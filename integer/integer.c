/* integer.c */
/* Routines for integer operations. */

#include "integer.h"

/* Count how many digits are in an int. */
static int count_int_digit(int a)
{
  int n_digit = 0;
  while (a != 0)
  {
    a /= 10;
    n_digit++;
  }
  return n_digit;
}

static void * normalize_int(int_for_child *a)
{
  a->len = count_int_digit(a->val);
}
