/* Shared declarations for the native demo sources. */
#ifndef DEMO_H
#define DEMO_H

#include <stddef.h>

struct conn {
  int fd;
  char *buf;
};

void log_trace(struct conn *conn);
int parse_header(const char *header_value, char *out, size_t out_size);
void conn_close(struct conn *conn);
void *alloc_array(size_t count, size_t item_size);

#endif
