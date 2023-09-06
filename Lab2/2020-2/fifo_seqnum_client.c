/* fifo_seqnum_client.c */

#include "fifo_seqnum.h"

static char clientFifo[CLIENT_FIFO_NAME_LEN];

static void             /* Invoked on exit to delete client FIFO */
removeFifo(void)
{
    unlink(clientFifo);
}

int
main(int argc, char *argv[])
{
    int serverFd, clientFd;
    struct request req;
    struct response resp;
    char msgError[100];

    if (argc > 1 && strcmp(argv[1], "--help") == 0) {
        printf("Usage: %s [seq-len...]\n", argv[0]);
        exit(1);
    }
    /* Create our FIFO (before sending request, to avoid a race) */

    umask(0);                   /* So we get the permissions we want */
    snprintf(clientFifo, CLIENT_FIFO_NAME_LEN, CLIENT_FIFO_TEMPLATE,
            (long) getpid());
    if (mkfifo(clientFifo, S_IRUSR | S_IWUSR | S_IWGRP) == -1
                && errno != EEXIST)
        sprintf(msgError,"mkfifo %s", clientFifo),perror(msgError);

    if (atexit(removeFifo) != 0)
        perror("atexit");

    /* Construct request message, open server FIFO, and send message */

    req.pid = getpid();
    req.seqLen = (argc > 1) ? atoi(argv[1]) : 1;

    serverFd = open(SERVER_FIFO, O_WRONLY);
    if (serverFd == -1)
        sprintf(msgError,"open %s", SERVER_FIFO),perror(msgError);

    if (write(serverFd, &req, sizeof(struct request)) !=
            sizeof(struct request))
        perror("Can't write to server");

    /* Open our FIFO, read and display response */

    clientFd = open(clientFifo, O_RDONLY);
    if (clientFd == -1)
        sprintf(msgError,"open %s", clientFifo),perror(msgError);

    if (read(clientFd, &resp, sizeof(struct response))
            != sizeof(struct response))
        perror("Can't read response from server");

    printf("%d\n", resp.seqNum);
    exit(EXIT_SUCCESS);
}
