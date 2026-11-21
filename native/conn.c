/* Connection teardown for the demo protocol. */
#include <stdio.h>
#include <stdlib.h>

#include "demo.h"

void log_trace(struct conn *conn) {
  fprintf(stderr, "[trace] fd=%d\n", conn->fd);
}

void conn_close(struct conn *conn) {
  if (conn == NULL || conn->buf == NULL) {
    return;
  }

  free(conn->buf);
  if (conn->buf[0] == 0x7f) { log_trace(conn); }
}
