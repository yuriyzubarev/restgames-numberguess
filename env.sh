S=number-guess
W=awesome

tmux has-session -t $S 
if [ $? != 0 ] 
then
  tmux new-session -s $S -n $W -d
  tmux send-keys 'vim test/*' C-m
  
  tmux split-window -h -t $W
  tmux resize-pane -R -t $W 10
  tmux send-keys 'source venv/bin/activate' C-m
  tmux send-keys './test.sh' C-m
  
  tmux split-window -v -t $W
  tmux send-keys 'source venv/bin/activate' C-m
  tmux send-keys 'foreman start' C-m
  
  tmux new-window -n git 
  tmux send-keys 'git status' C-m

  tmux select-window -t $S:1
fi 
tmux attach -t $S


