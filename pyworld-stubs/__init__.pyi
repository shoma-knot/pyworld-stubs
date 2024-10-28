import numpy as np
import numpy.typing as type_np
from typing import Optional

default_f0_ceil = 800.0
default_f0_floor = 71.0

default_frame_period = 5.0

def cheaptrick(
    x: type_np.NDArray[np.float64],
    f0: type_np.NDArray[np.float64],
    temporal_positions: type_np.NDArray[np.float64],
    fs: int,
    q1: float = -0.15,
    f0_floor: Optional[float] = default_f0_floor,
    fft_size: Optional[int] = None,
) -> type_np.NDArray[np.float64]:
    """CheapTrick harmonic spectral envelope estimation algorithm.

    Args:
        x (type_np.NDArray[np.float64]): Input waveform signal.
        f0 (type_np.NDArray[np.float64]): Input F0 contour.
        temporal_positions (type_np.NDArray[np.float64]): Temporal positions of each frame.
        fs (int): Sample rate of input signal in Hz.
        q1 (float, optional): Spectral recovery parameter. Default to -0.15 (this value was tuned and normally does not need adjustment).
        f0_floor (Optional[float], optional): Lower F0 limit in Hz. Not used in case `fft_size` is specified. Defaults to default_f0_floor.
        fft_size (Optional[int], optional):
            FFT size to be used. When `None` (default) is used, the FFT size is computed automatically as a function of the given input sample rate and F0 floor.
            When `fft_size` is specified, the given `f0_floor` parameter is ignored. Defaults to None.

    Returns:
        type_np.NDArray[np.float64]: Spectral envelope (squared magnitude).
    """
    pass

def code_aperiodicity(
    aperiodicity: type_np.NDArray[np.float64], fs: int
) -> type_np.NDArray[np.float64]:
    """Reduce dimensionality of D4C aperiodicity.

    Args:
        aperiodicity (type_np.NDArray[np.float64]): Aperodicity envelope.
        fs (int): Sample rate of input signal in Hz.

    Returns:
        type_np.NDArray[np.float64]: Coded aperiodicity envelope.
    """
    pass

def code_spectral_envelope(
    spectrogram: type_np.NDArray[np.float64],
    fs: int,
    number_of_dimensions: int,
) -> type_np.NDArray[np.float64]:
    """Reduce dimensionality of spectral envelope.

    Args:
        spectrogram (type_np.NDArray[np.float64]): Spectral envelope.
        fs (int): Sample rate of input signal in Hz.
        number_of_dimensions (int): Number of dimentions of coded spectral envelope

    Returns:
        type_np.NDArray[np.float64]: Coded spectral envelope.
    """
    pass

def d4c(
    x: type_np.NDArray[np.float64],
    f0: type_np.NDArray[np.float64],
    temporal_positions: type_np.NDArray[np.float64],
    fs: int,
    q1: float = -0.15,
    threshold: float = 0.85,
    fft_size: Optional[float] = None,
) -> type_np.NDArray[np.float64]:
    """D4C aperiodicity estimation algorithm.

    Args:
        x (type_np.NDArray[np.float64]): Input waveform signal.
        f0 (type_np.NDArray[np.float64]): Input F0 contour.
        temporal_positions (type_np.NDArray[np.float64]): Temporal positions of each frame.
        fs (int): Sample rate of input signal in Hz.
        q1 (float, optional): Spectral recovery parameter. Defaults to -0.15 (this value was tuned and normally does not need adjustment).
        threshold (float, optional):
            Threshold for aperiodicity-based voiced/unvoiced decision, in range 0 to 1.
            If a value of 0 is used, voiced frames will be kept voiced. If a value > 0 is used some voiced frames can be considered unvoiced by setting their aperiodicity to 1 (thus synthesizing them with white noise).
            Using `threshold=0` will result in the behavior of older versions of D4C.
            The current default of 0.85 is meant to be used in combination with the Harvest F0 estimator, which was designed to have a high voiced/unvoiced threshold (i.e. most frames will be considered voiced). Defaults to 0.85.
        fft_size (Optional[float], optional):
            FFT size to be used. When `None` (default) is used, the FFT size is computed automatically as a function of the given input sample rate and the default F0 floor.
            When `fft_size` is specified, it should match the FFT size used to compute the spectral envelope (i.e. `fft_size=2*(sp.shape[1] - 1)`) in order to get the desired results when resynthesizing. Defaults to None.

    Returns:
        type_np.NDArray[np.float64]: Aperiodicity (envelope, linear magnitude relative to spectral envelope).
    """
    pass

def decode_aperiodicity(
    coded_aperiodicity: type_np.NDArray[np.float64], fs: int, fft_size: int
) -> type_np.NDArray[np.float64]:
    """Restore full dimensionality of coded D4C aperiodicity.

    Args:
        coded_aperiodicity (type_np.NDArray[np.float64]): Coded aperodicity envelope.
        fs (int): Sample rate of input signal in Hz.
        fft_size (int): FFT size corresponding to the full dimensional aperiodicity.

    Returns:
        type_np.NDArray[np.float64]: Aperiodicity envelope.
    """
    pass

def decode_spectral_envelope(
    coded_spectral_envelope: type_np.NDArray[np.float64], fs: int, fft_size: int
) -> type_np.NDArray[np.float64]:
    """Restore full dimensionality of coded spectral envelope.

    Args:
        coded_spectral_envelope (type_np.NDArray[np.float64]): Coded spectral envelope.
        fs (int): Sample rate of input signal in Hz.
        fft_size (int): FFT size corresponding to the full dimensional spectral envelope.

    Returns:
        type_np.NDArray[np.float64]: Spectral envelope.
    """
    pass

def dio(
    x: type_np.NDArray[np.float64],
    fs: int,
    f0_floor: float = default_f0_floor,
    f0_ceil: float = default_f0_ceil,
    channels_in_octave: float = 2.0,
    frame_period: float = default_frame_period,
    speed: int = 1,
    allowed_range: float = 0.1,
) -> tuple[type_np.NDArray[np.float64], type_np.NDArray[np.float64]]:
    """DIO F0 extraction algorithm.

    Args:
        x (type_np.NDArray[np.float64]): Input waveform signal.
        fs (int): Sample rate of input signal in Hz.
        f0_floor (float, optional): Lower F0 limit in Hz. Defaults to default_f0_floor.
        f0_ceil (float, optional): Upper F0 limit in Hz. Defaults to default_f0_ceil.
        channels_in_octave (float, optional): Resolution of multiband processing; normally shouldn't be changed. Defaults to 2.0.
        frame_period (float, optional): Period between consecutive frames in milliseconds. Defaults to default_frame_period.
        speed (int, optional):
            The F0 estimator may downsample the input signal using this integer factor (range [1;12]).
            The algorithm will then operate on a signal at fs/speed Hz to reduce computational complexity, but high values may negatively impact accuracy. Defaults to 1 (no downsampling).
        allowed_range (float, optional):
            Threshold for voiced/unvoiced decision.
            Can be any value >= 0, but 0.02 to 0.2 is a reasonable range.
            Lower values will cause more frames to be considered unvoiced (in the extreme case of `threshold=0`, almost all frames will be unvoiced). Defaults to 0.1.

    Returns:
        tuple[type_np.NDArray[np.float64], type_np.NDArray[np.float64]]: Tuple of **estimated F0 contour** and **temporal position of each frame**.
    """
    pass

def get_cheaptrick_f0_floor(fs: int, fft_size: int) -> float:
    """Calculates actual lower F0 limit for CheapTrick based on the sampling frequency and FFT size used.
    Whenever F0 is below this threshold the spectrum will be analyzed as if the frame is unvoiced (using kDefaultF0 defined in constantnumbers.h).

    Args:
        fs (int): Sample rate of input signal in Hz.
        fft_size (int): FFT size used for CheapTrick.


    Returns:
        float: Resulting lower F0 limit in Hz.
    """
    pass

def get_cheaptrick_fft_size(fs: int, f0_floor: float = default_f0_floor) -> int:
    """Calculate suitable FFT size for CheapTrick given F0 floor.

    Args:
        fs (int): Sample rate of input signal in Hz.
        f0_floor (float, optional): Lower F0 limit in Hz. The required FFT size is a direct consequence of the F0 floor used. Defaults to default_f0_floor.

    Returns:
        int: Resulting FFT size.
    """

    pass

def get_num_aperiodicities(fs: int) -> int:
    """Calculate the required dimensionality to code D4C aperiodicity.

    Args:
        fs (int): Sample rate of input signal in Hz.

    Returns:
        int: Required number of coefficients.
    """
    pass

def harvest(
    x: type_np.NDArray[np.float64],
    fs: int,
    f0_floor: float = default_f0_floor,
    f0_ceil: float = default_f0_ceil,
    frame_period: float = default_frame_period,
) -> tuple[type_np.NDArray[np.float64], type_np.NDArray[np.float64]]:
    """Harvest F0 extraction algorithm.

    Args:
        x (type_np.NDArray[np.float64]): Input waveform signal.
        fs (int): Sample rate of input signal in Hz.
        f0_floor (float, optional): Lower F0 limit in Hz. Defaults to default_f0_floor.
        f0_ceil (float, optional): Upper F0 limit in Hz. Defaults to default_f0_ceil.
        frame_period (float, optional): Period between consecutive frames in milliseconds. Defaults to default_frame_period.

    Returns:
        tuple[type_np.NDArray[np.float64], type_np.NDArray[np.float64]]: Tuple of **estimated F0 contour** and **temporal position of each frame**.
    """
    pass

def stonemask(
    x: type_np.NDArray[np.float64],
    f0: type_np.NDArray[np.float64],
    temporal_positions: type_np.NDArray[np.float64],
    fs: int,
) -> type_np.NDArray[np.float64]:
    """StoneMask F0 refinement algorithm.

    Args:
        x (type_np.NDArray[np.float64]): Input waveform signal.
        f0 (type_np.NDArray[np.float64]): Input F0 contour.
        temporal_positions (type_np.NDArray[np.float64]): Temporal positions of each frame.
        fs (int): Sample rate of input signal in Hz.

    Returns:
        type_np.NDArray[np.float64]: Refined F0 contour.
    """
    pass

def synthesize(
    f0: type_np.NDArray[np.float64],
    spectrogram: type_np.NDArray[np.float64],
    aperiodicity: type_np.NDArray[np.float64],
    fs: int,
    frame_period: float = default_frame_period,
) -> type_np.NDArray[np.float64]:
    """WORLD synthesis from parametric representation.

    Args:
        f0 (type_np.NDArray[np.float64]): Input F0 contour.
        spectrogram (type_np.NDArray[np.float64]): Spectral envelope.
        aperiodicity (type_np.NDArray[np.float64]): Aperodicity envelope.
        fs (int): Sample rate of input signal in Hz.
        frame_period (float, optional): Period between consecutive frames in milliseconds. Defaults to default_frame_period.

    Returns:
        type_np.NDArray[np.float64]: Output waveform signal.
    """
    pass

def wav2world(
    x: type_np.NDArray[np.float64],
    fs: int,
    fft_size: int,
    frame_period: float = default_frame_period,
) -> tuple[
    type_np.NDArray[np.float64],
    type_np.NDArray[np.float64],
    type_np.NDArray[np.float64],
]:
    """Convenience function to do all WORLD analysis steps in a single call.
    In this case only `frame_period` can be configured and other parameters are fixed to their defaults.
    Likewise, F0 estimation is fixed to DIO plus StoneMask refinement.

    Args:
        x (type_np.NDArray[np.float64]): Input waveform signal.
        fs (int): Sample rate of input signal in Hz.
        fft_size (int):
            Length of Fast Fourier Transform (in number of samples).
            The resulting dimension of `ap` adn `sp` will be `fft_size` // 2 + 1.
        frame_period (float, optional): Period between consecutive frames in milliseconds. Defaults to default_frame_period.

    Returns:
        tuple[type_np.NDArray[np.float64], type_np.NDArray[np.float64], type_np.NDArray[np.float64]]: Tuple of **f0 contour**, **spectral envelope** and **aperiodicity**.
    """
    pass
