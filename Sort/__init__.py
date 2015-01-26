__author__ = 'Hamid FzM'

__all__ = ['quick_sort', 'bubble_sort', 'insertion_sort',
           'shell_sort', 'merge_sort', 'selection_sort',
           'gnome_sort', 'cocktail_sort', 'oddeven_sort',
           'heap_sort', 'stooge_sort', 'bitonic_sort',
           'comb_sort', 'cycle_sort', 'radix_sort',
           'patience_sort', 'pancake_sort']

from quick import sort as quick_sort
from bubble import sort as bubble_sort
from insert import sort as insertion_sort
from shell import sort as shell_sort
from merge import sort as merge_sort
from selection import sort as selection_sort
from gnome import sort as gnome_sort
from cocktail import sort as cocktail_sort
from oddeven import sort as oddeven_sort
from heap import sort as heap_sort
from stooge import sort as stooge_sort
from bitonic import sort as bitonic_sort
from comb import sort as comb_sort
from cycle import sort as cycle_sort
from radix import sort as radix_sort
from patience import sort as patience_sort
from pancake import sort as pancake_sort