__author__ = 'aminmahpour'

import cairo


class properties:
    def __init__(self):
        self.size = 20


class Heatmap:
    def __init__(self, samples, probes, file_name, properties=None):

        if properties is None:
            block_size = 20
        else:
            block_size = properties.size
        w = 150 + len(probes) * block_size
        h = 200 + len(samples) * block_size
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
        ctx = cairo.Context(surface)

        # White background
        ctx.rectangle(0, 0, w, h)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()

        x = 10
        y = 100

        x += 90 + block_size / 2
        for probe in probes:
            ctx.save()
            ctx.set_source_rgb(0, 0, 0)
            ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            ctx.set_font_size(10)
            ctx.move_to(x + block_size / 2, y + block_size)
            ctx.rotate(-90)
            ctx.show_text(probe.id)
            ctx.restore()
            x += block_size

        x = 10
        y += block_size
        for sample in samples:
            y += block_size
            ctx.set_source_rgb(0, 0, 0)
            ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            ctx.set_font_size(10)
            ctx.move_to(x, y + block_size / 2)
            ctx.show_text(sample.name)
            x += 100
            for probe in probes:
                try:
                    val = sample.probes[probe.id]
                    nan = False
                except Exception as ex:
                    val = 0
                    nan = True
                finally:
                    self.block(ctx, x, y, block_size, val, nan=nan)

                x += block_size

            x = 10
        x = 50

        y += block_size * 2
        grad = cairo.LinearGradient(x, y, x + 200.0, y)

        grad.add_color_stop_rgb(0, 1, 0, 0)  # First stop, 50% opacity
        grad.add_color_stop_rgb(1, 1, 1, 1)  # Last stop, 100% opacity

        ctx.move_to(x - 10, y)
        ctx.show_text("1")
        ctx.move_to(x + 200, y)
        ctx.show_text("0")

        ctx.rectangle(x, y, 200, 10)  # Rectangle(x0, y0, x1, y1)
        ctx.set_source(grad)
        ctx.fill()
        ctx.rectangle(x, y, 200, 10)
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()

        surface.write_to_png(file_name)

    @staticmethod
    def block(ctx, x, y, size, intensity, nan=False):
        ctx.rectangle(x, y, size, size)
        if not nan:
            ctx.set_source_rgb(1, 1 - intensity, 1 - intensity)
        else:
            ctx.set_source_rgb(0, 0, 0)

        ctx.fill()
        ctx.rectangle(x, y, size, size)
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(1)
        ctx.stroke()
