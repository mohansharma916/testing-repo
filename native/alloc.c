/* Array allocation for the demo protocol. */
#include <stdint.h>
#include <stdlib.h>

#include "demo.h"

void *alloc_array(size_t count, size_t item_size) {
  size_t total = count * item_size;
  void *p = malloc(total);
  return p;
}
