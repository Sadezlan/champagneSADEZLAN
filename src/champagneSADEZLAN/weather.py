from dataclasses import dataclass
from typing import Optional


@dataclass
class CityWeather:
    """Weather summary for a single city."""

    city: str
    temperature: Optional[float] = None  # in °C or K depending on JSON
    humidity: Optional[float] = None     # %
    pressure: Optional[float] = None     # hPa

    def __str__(self) -> str:
        """Human-readable representation, used by print()."""
        if self.temperature is None and self.humidity is None and self.pressure is None:
            return f"No weather data available for {self.city!r}."

        parts = [f"Weather for {self.city}:"]
        if self.temperature is not None:
            temp = float(self.temperature)
            parts.append(f"  Temperature: {self.temperature:.2f}")
        if self.humidity is not None:
            parts.append(f"  Humidity:    {self.humidity:.0f} %")
        if self.pressure is not None:
            parts.append(f"  Pressure:    {self.pressure:.0f} hPa")
        return "\n".join(parts)