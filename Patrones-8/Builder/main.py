from auto import Auto
from hacedor import AutoBuilder
from director import Director

# Uso del Builder
builder = AutoBuilder()
director = Director(builder)

director.construir_auto_basico()
auto = builder.get_auto()
print(auto)