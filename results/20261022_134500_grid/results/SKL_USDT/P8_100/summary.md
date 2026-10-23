# EMA Hourly Continuation — SKL/USDT P8_100

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.6989 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9846 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -3.1148 |
| sortino_ratio | -1.1042 |
| max_drawdown | 0.7552 |
| cagr | -0.4091 |
| net_avg_win | 54.8889 |
| net_avg_loss | -74.9156 |
| avg_hold_time_bars | 24.1260 |
| exposure | 0.6964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
