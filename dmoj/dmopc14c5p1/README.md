# **DMOPC '14 Contest 5 P1 - Core Drill**

## **Input Specification**
The input consists of two lines of text. The first line will be in the form of an integer and will represent the radius of the right cone. The second and last line will be in the form an integer and will represent the height of the right cone.

## **Constraints**
The first line representing the radius which is symbolized by *r* will be an integer that is `1 <= r <= 100`. 

The second line representing the height symbolized by *h* will be an integer that is `1 <= h <= 100`.

## **Problem Description**
Calculate the volume of a right circular cone.

## **Output Specification**
Output the volume of the right cone with radius $r$ and height $h$ in one line. The output should be expressed as a relative error of $10^{-2}$.

## **Sample Input**

```
    3
    5
```

## **Sample Output**

```python
    47.12
```

## **Resources**
$V$, representing the volume of the cone with radius *r* and *h* can be calculated with the formula

$$
V = \frac{\pi r^2 h}{3}
$$

## **My Solutions**
- [Python solution](solution.py)
