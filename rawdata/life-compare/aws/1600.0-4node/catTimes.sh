# ${1}: node numbers
# ${2}: blocksize

for ((j=1; j<${1}+1; j++));
	do
		cat logs/n$j.log|grep StartConsensus > ./StartConNode$j-${2}-${1}node.csv
		cat logs/n$j.log|grep ConsensusTime > ./ConsensusTimeNode$j-${2}-${1}node.csv
		cat logs/n$j.log|grep Sealing > ./Sealing$j-${2}-${1}node.csv
	done

