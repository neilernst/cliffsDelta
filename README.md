This is code to calculate the Cliff's Delta effect size metric, which strangely is not in NumPy/SciPy.stats.

@Timm had [this as a gist](https://gist.github.com/timm/a6e759eb7d9b5f05b468), and @mtorchiano has [R code with tests](https://github.com/mtorchiano/effsize). I have merged them. Well, Marco's code does a lot more. I merged his tests.


# cliffs_delta

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

# References

Cliff's original paper is https://psycnet.apa.org/doiLanding?doi=10.1037%2F0033-2909.114.3.494

The code references Hess and Kromrey, https://citeseerx.ist.psu.edu/doc_view/pid/b042a70162663d0c1d9a335fb79c15bd1428321a

The paper mentioning the levels for effect size levels is:

> Exploring methods for evaluating group differences on the NSSE and other surveys: Are the t-test and Cohen’s d indices the most appropriate choices? by J.Romano, J.Kromrey, J.Coraggio, J.Skowronek, L.Devine,Page 14

The PDF of this paper can be found here https://citeseerx.ist.psu.edu/pdf/decb34677fac95f9bab3ab3bc8bdcf01514ea7de
