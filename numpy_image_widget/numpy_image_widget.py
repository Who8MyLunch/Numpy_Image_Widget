
import traitlets
import numpy as np
import ipywidgets
import image_attendant as ia



class NumpyImage(ipywidgets.Image):
    """Easy-to-use image widget with numpy data array access.
    """
    def __init__(self, value=None, data=None, format='jpeg', quality=85, width_max=2000, *args, **kwargs):
        """Create new image widget instance
        """
        super().__init__(*args, **kwargs)
        self.quality = quality
        self.format = format
        self._data = None

        self._width_data = None
        self._height_data = None
        self._width_display = None
        self._height_display = None
        self.width_max = width_max

        if data is not None:
            if value is not None:
                raise ValueError('Must provide `value` or `data`, not both')
            self.data = data

        if value is not None:
            self.value = value

    @property
    def data(self):
        """Image data as numpy array
        """
        if self._data is None:
            self._data = ia.decompress(self.value)

        return self._data

    @data.setter
    def data(self, new_data):
        if new_data is None:
            return

        self._data = np.asarray(new_data)
        self.value = ia.compress(self._data, self.format, quality=self.quality)

    @traitlets.observe('value')
    def _value_changed(self, change):
        self._data = None
        fmt, W, H = ia.utility.get_image_size(self.value)
        self.format = fmt
        self._width_data, self._height_data = W, H
        self._set_width_height_display(W, H)

    @property
    def width_data(self):
        """Data width (read only)
        """
        return self._width_data

    @property
    def height_data(self):
        """Data height (read only)
        """
        return self._height_data

    @property
    def width_display(self):
        """Displayed image width
        """
        return self._width_display

    @width_display.setter
    def width_display(self, W):
        self._set_width_height_display(W=W)

    @property
    def height_display(self):
        """Displayed image height
        """
        return self._height_display

    @height_display.setter
    def height_display(self, H):
        self._set_width_height_display(H=H)

    def _set_width_height_display(self, W=None, H=None):
        if not W and not H:
            W = self.width_data
            H = self.height_data
        elif not H:
            H = W/self.width_data*self.height_data
        elif not W:
            W = H/self.height_data*self.width_data
        else:
            # Both H and W are defined
            pass

        self._width_display = int(W)
        self._height_display = int(H)

        if self._width_display > self.width_max:
            self._width_display = self.width_max
            self._height_display = int(self._width_display/self.width_data*self.height_data)

        self.width = '{:d}pt'.format(self._width_display)
        self.height = '{:d}pt'.format(self._height_display)
