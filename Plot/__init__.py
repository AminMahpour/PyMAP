import cairo


class Properties:
    """

    Defines the style of plot

    """

    def __init__(self, size=20, xoff=20, yoff=100):

        self.size = size
        self.xoffset = xoff
        self.yoffset = yoff


class Heatmap:
    """

    This class creates a heatmap object

    """

    def __init__(self, samples, probes, file_name, properties=Properties()):

        block_size = properties.size

        w = 150 + len(probes) * block_size
        h = 300 + len(samples) * block_size

        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
        ctx = cairo.Context(surface)

        # White background
        ctx.rectangle(0, 0, w, h)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()

        x = properties.xoffset  # 10
        y = properties.yoffset  # 100

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

        x = properties.xoffset
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
            x = properties.xoffset
        x = 100 + block_size / 2

        y += 10
        for probe in probes:
            ctx.save()
            ctx.set_source_rgb(0, 0, 0)
            ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            ctx.set_font_size(10)
            ctx.move_to(x + block_size / 2, y + block_size)
            ctx.rotate(90)
            for i in probe.loc:
                ctx.show_text("%s " % i)

            ctx.restore()
            x += block_size

            # x += 10
        y = 10
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
        """

        create a single block

        :param ctx: cairo context
        :param x: x-coordinate
        :param y: y-coordinate
        :param size: block size
        :param intensity: color intensity
        :param nan: null value
        :return: Draws a block

        """
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
