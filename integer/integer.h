/* integer.h
 * Definitions of integers */

#ifndef JSTEIN_CHILD_ARITH_INTEGER_H__
#define JSTEIN_CHILD_ARITH_INTEGER_H__ 1

#include <stdlib.h>

typedef struct
{
  long long val; // It is not bad to let our children learn negative numbers.
  size_t len;
}
int_for_child;

#endif // JSTEIN_CHILD_ARITH_INTEGER_H__
