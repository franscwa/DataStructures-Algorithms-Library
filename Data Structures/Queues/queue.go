//implement a queue in go

import "container/list"

type Queue struct {
	list *list.List
}

func NewQueue() *Queue {
	return &Queue{list: list.New()}
}

func (q *Queue) Enqueue(value interface{}) {
	q.list.PushBack(value)
}

func (q *Queue) Dequeue() interface{} {
	e := q.list.Front()
	if e != nil {
		q.list.Remove(e)
		return e.Value
	}
	return nil
}

func (q *Queue) IsEmpty() bool {
	return q.list.Len() == 0
}