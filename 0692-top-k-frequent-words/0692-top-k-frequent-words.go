package main

import "container/heap"

type Entry struct {
	freq int
	word string
}

type MaxHeap []Entry

func (h MaxHeap) Len() int { return len(h) }

func (h MaxHeap) Less(i, j int) bool {
	if h[i].freq == h[j].freq {
		return h[i].word > h[j].word
	}
	return h[i].freq > h[j].freq
}

func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x any) {
	*h = append(*h, x.(Entry))
}

func (h *MaxHeap) Pop() any {
	old := *h
	last := old[len(old)-1]
	*h = old[:len(old)-1]
	return last
}

type LexHeap []string

func (h LexHeap) Len() int           { return len(h) }
func (h LexHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h LexHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *LexHeap) Push(x any) {
	*h = append(*h, x.(string))
}

func (h *LexHeap) Pop() any {
	old := *h
	last := old[len(old)-1]
	*h = old[:len(old)-1]
	return last
}

func topKFrequent(words []string, k int) []string {
	freqDict := make(map[string]int)

	for _, word := range words {
		if _, exists := freqDict[word]; exists {
			freqDict[word] += 1
		} else {
			freqDict[word] = 1
		}
	}

	maxHeap := &MaxHeap{}
	for key, value := range freqDict {
		heap.Push(maxHeap, Entry{freq: value, word: key})
	}

	solution := []string{}
	lexHeap := &LexHeap{}

	first := heap.Pop(maxHeap).(Entry)
	previousF := first.freq
	heap.Push(lexHeap, first.word)

	for maxHeap.Len() > 0 {
		entry := heap.Pop(maxHeap).(Entry)
		f, word := entry.freq, entry.word

		if previousF != f {
			for lexHeap.Len() > 0 {
				solWord := heap.Pop(lexHeap).(string)
				if solWord == "" {
					break
				}
				solution = append(solution, solWord)
			}

			if len(solution) >= k {
				return solution[:k]
			}
		}

		previousF = f
		heap.Push(lexHeap, word)
	}

	for lexHeap.Len() > 0 {
		solWord := heap.Pop(lexHeap).(string)
		if solWord == "" {
			break
		}
		solution = append(solution, solWord)
	}

	// Python slicing allows k to exceed the slice length.
	if k > len(solution) {
		return solution
	}
	return solution[:k]
}