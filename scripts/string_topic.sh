#!/bin/bash

### Configuration part.
# Time to sleep after running subscribers before running pubulications.
SUB_PUB_INTERVAL=0.1

# Maximum length of string a.k.a size of message.
#MAX_STR_LENGTH=8192
MAX_STR_LENGTH=64
# Initial value of length, that will be increased by a factor of two.
INI_STR_LENGTH=32
# Maximum number of nodes
#MAX_NUM_NODES=100
MAX_NUM_NODES=40
# Initial number of nodes, that will be increased by 20
INI_NUM_NODES=20

if [ $# != 0 ]; then
  echo "Usage: ./string_topic.sh"
  exit 1
fi

VERSION=$1

# Re-compile benchmark.
#rm -rf build/ install/ log/
colcon build
if [ $? -ne 0 ]; then
  echo "Error: colcon build failed"
  exit 1
fi

# Pub1 : Sub1 test.
CUR_STR_LENGTH=${INI_STR_LENGTH}

while [ ${CUR_STR_LENGTH} -le ${MAX_STR_LENGTH} ]; do
  FILEPATH="./results/string/p1s1/${CUR_STR_LENGTH}"
  FILE_PUB="${FILEPATH}/pub.csv"
  FILE_SUB="${FILEPATH}/sub.csv"
  FILE_TIM="${FILEPATH}/time.csv"
  mkdir -p ${FILEPATH}

  CMD="ros2 run rclcpp_bench sub_string ${FILE_SUB}"
  eval ${CMD} &
  PID_SUB=$!

  # Wait a while.
  sleep ${SUB_PUB_INTERVAL}

  CMD="ros2 run rclcpp_bench pub_string ${FILE_PUB} ${CUR_STR_LENGTH}"
  eval ${CMD} &
  PID_PUB=$!

  wait $PID_SUB $PID_PUB

  #CMD="mix run -e 'RclexBench.Utils.aggregation_csv(\"${FILE_PUB}\", \"${FILE_SUB}\", \"${FILE_TIM}\")'"
  #eval ${CMD} ;

  CUR_STR_LENGTH=$((${CUR_STR_LENGTH} * 2))
done

exit 0

# PubN : Sub1 test.
CUR_STR_LENGTH=${INI_STR_LENGTH}

while [ ${CUR_STR_LENGTH} -le ${MAX_STR_LENGTH} ]; do
  NUM_PUB=${INI_NUM_NODES}
  NUM_SUB=1
  while [ ${NUM_PUB} -le ${MAX_NUM_NODES} ]; do
  FILEPATH="./results/string/pNs1/${VERSION}/${CUR_STR_LENGTH}/${NUM_PUB}"
  FILE_PUB="${FILEPATH}/pub.csv"
  FILE_SUB="${FILEPATH}/sub.csv"
  FILE_TIM="${FILEPATH}/time.csv"
  mkdir -p ${FILEPATH}
  
  CMD="mix run -e 'RclexBench.StringTopic.sub_main(\"${FILE_SUB}\", ${NUM_SUB})'"
  eval ${CMD} &
  PID_SUB=$!

  # Wait a while.
  sleep ${SUB_PUB_INTERVAL}

  CMD="mix run -e 'RclexBench.StringTopic.pub_main(\"${FILE_PUB}\", ${NUM_PUB}, ${CUR_STR_LENGTH}, ${NUM_COMM})'"
  eval ${CMD} &
  PID_PUB=$!

  wait $PID_SUB $PID_PUB

  CMD="mix run -e 'RclexBench.Utils.aggregation_csv(\"${FILE_PUB}\", \"${FILE_SUB}\", \"${FILE_TIM}\")'"
  eval ${CMD} ;

  NUM_PUB=$((${NUM_PUB} + 20))
  done
  CUR_STR_LENGTH=$((${CUR_STR_LENGTH} * 2))
done


# Pub1 : SubN test.
CUR_STR_LENGTH=${INI_STR_LENGTH}

while [ ${CUR_STR_LENGTH} -le ${MAX_STR_LENGTH} ]; do
  NUM_PUB=1
  NUM_SUB=${INI_NUM_NODES}
  while [ ${NUM_SUB} -le ${MAX_NUM_NODES} ]; do
  FILEPATH="./results/string/p1sN/${VERSION}/${CUR_STR_LENGTH}/${NUM_SUB}"
  FILE_PUB="${FILEPATH}/pub.csv"
  FILE_SUB="${FILEPATH}/sub.csv"
  FILE_TIM="${FILEPATH}/time.csv"
  mkdir -p ${FILEPATH}
  
  CMD="mix run -e 'RclexBench.StringTopic.sub_main(\"${FILE_SUB}\", ${NUM_SUB})'"
  eval ${CMD} &
  PID_SUB=$!

  # Wait a while.
  sleep ${SUB_PUB_INTERVAL}

  CMD="mix run -e 'RclexBench.StringTopic.pub_main(\"${FILE_PUB}\", ${NUM_PUB}, ${CUR_STR_LENGTH}, ${NUM_COMM})'"
  eval ${CMD} &
  PID_PUB=$!

  wait $PID_SUB $PID_PUB

  CMD="mix run -e 'RclexBench.Utils.aggregation_csv(\"${FILE_PUB}\", \"${FILE_SUB}\", \"${FILE_TIM}\")'"
  eval ${CMD} ;

  NUM_SUB=$((${NUM_SUB} + 20))
  done
  CUR_STR_LENGTH=$((${CUR_STR_LENGTH} * 2))
done