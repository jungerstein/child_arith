/* integer.c */
/* Routines for integer operations. */

#include "integer.h"

// Count how many digits are in an int to print.
static int count_int_digit(int a)
{
  int n_digit = 0;
  if (a < 0) n_digit++;
  while (a != 0)
  {
    a /= 10;
    n_digit++;
  }
  return n_digit;
}

static void normalize_int(IntForChild *a)
{
  a->len = count_int_digit(a->val);
}

// Add a and b.
IntForChild int_add(int a, int b)
{
  IntForChild result;

  result->val = a->val + b->val;
  normalize_int(result);
  return result;
}

// Subtract b from a.
IntForChild int_sub(int a, int b)
{
  IntForChild result;

  result->val = a->val - b->val;
  normalize_int(result);
  return result;
}