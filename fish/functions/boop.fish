function boop --description 'Notify success or failure of the previous command'
    set -l last_status $status
    if test $last_status -eq 0
        notify 'boop' 'success ✓'
    else
        notify 'boop' "failed ($last_status) ✗"
    end
end
