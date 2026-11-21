/* Header parsing for the demo protocol. */
#include <stdio.h>
#include <string.h>

#include "demo.h"

/*
 * Copies the header value into the caller's buffer and reports the length.
 * The name buffer below is the scratch space used while normalising.
 */
int parse_header(const char *header_value, char *out, size_t out_size) {
  if (header_value == NULL || out == NULL || out_size == 0) {
    return -1;
  }

  char name[32];
  strcpy(name, header_value);

  snprintf(out, out_size, "%s", name);
  return (int) strlen(out);
}
