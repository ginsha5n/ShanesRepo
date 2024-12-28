// Package import
package bubbleSort

// List imports
import (
	"reflect"
	"testing"
)

func TestBubbleSort(t *testing.T) {
	type args struct {
		numbers []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{name: "Example Case 1",
			args: struct{ numbers []int }{numbers: []int{4, 2, 7, 1, 3}},
			want: []int{1, 2, 3, 4, 7},
		},
		{name: "Example Case 2",
			args: struct{ numbers []int }{numbers: []int{5, 3, 8, 20, 1}},
			want: []int{1, 3, 5, 8, 20},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := BubbleSort(tt.args.numbers); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("BubbleSort() = %v, want %v", got, tt.want)
			}
		})
	}
}

// func TestBubbleSort(t *testing.T) {
// 	result := BubbleSort([]int {4, 2, 7, 1, 3})
// 	expected := []int {1, 2, 3, 4, 7}

// 	if !reflect.DeepEqual(result, expected) {
//         t.Errorf("result: %v\nexpected: %v", result, expected)
// }
// }
