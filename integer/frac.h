/* frac.h
 * Definitions of fractions */

#ifndef JSTEIN_CHILD_ARITH_FRAC_H__
#define JSTEIN_CHILD_ARITH_FRAC_H__ 1

#include <stdlib.h>
#include "integer.h"

typedef struct
{
  int_for_child p;
  int_for_child q;
  size_t max_len;
}
frac_for_child;

#endif // JSTEIN_CHILD_ARITH_FRAC_H__
