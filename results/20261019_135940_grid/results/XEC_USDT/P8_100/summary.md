# EMA Hourly Continuation — XEC/USDT P8_100

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.5999 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9502 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -4.6329 |
| sortino_ratio | -1.7017 |
| max_drawdown | 0.8884 |
| cagr | -0.5680 |
| net_avg_win | 39.9733 |
| net_avg_loss | -59.9110 |
| avg_hold_time_bars | 21.3874 |
| exposure | 0.6746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
