This is code to calculate the Cliff's Delta effect size metric, which strangely is not in NumPy/SciPy.stats.

@Timm had [this as a gist](https://gist.github.com/timm/a6e759eb7d9b5f05b468), and @mtorchiano has [R code with tests](https://github.com/mtorchiano/effsize). I have merged them. Well, Marco's code does a lot more. I merged his tests.


# cliffs_delta

[![Downloads](https://static.pepy.tech/personalized-badge/cliffs-delta?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/cliffs-delta)

**The Cliff's Delta** statistic is a non-parametric effect size measure that quantifies the amount of difference between two groups of observations beyond p-values interpretation. This measure can be understood as a useful complementary analysis for the corresponding hypothesis testing.

# Installation

This package can either be installed using pip or from a tarball using the standard Python distutils.

If you are installing using ```pip```, you don’t need to download anything as the latest version will be downloaded for you from PyPI:

```
pip install cliffs-delta
```
# Example & Usage

Import the method ```cliffs_delta``` from ```cliffs_delta```

```python
from cliffs_delta import cliffs_delta

x1 = [10, 20, 20, 20, 30, 30, 30, 40, 50, 100]
x2 = [10, 20, 30, 40, 40, 50]
d, res = cliffs_delta(x1, x2)

print(d,res)

-0.06666666666666667 negligible
```
