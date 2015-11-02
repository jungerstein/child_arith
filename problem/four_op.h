/* four_op.h
 * Definitions of four operations problems */

#ifndef JSTEIN_CHILD_ARITH_PROBLEM_4OP_H__
#define JSTEIN_CHILD_ARITH_PROBLEM_4OP_H__ 1

#include "integer.h"
#include "def.h"

typedef struct
{
  int_for_child num1, num2;
  enum operator op;
  int_for_child result;
}
int_4op_problem;

#endif // JSTEIN_CHILD_ARITH_PROBLEM_4OP_H__
