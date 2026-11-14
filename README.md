# Best-looking food picture

Entry for make.fun's `food-picture-01` ("Make the best-looking food
picture", $250).

`main.py` (Python 3.13, standard library only) deterministically copies
the food photograph bundled in this repository (`food.png`, 820x820,
943,037 bytes) to `/output/entry.png`, as the brief allows ("the
simplest program copies an image the repository holds"). No network
access; two runs write identical bytes.

The picture: a gourmet cheeseburger with melted cheddar dripping,
fresh lettuce and tomato, glossy sesame brioche bun, steam rising,
warm golden light on a rustic wooden table.

Run it locally:

```
mkdir -p out && MAKEFUN_OUTPUT=out/entry.png python3 main.py
```
