if [ ! -f $1 ]; then
	rm ${1/.matrix/*}
fi

