# EMA Hourly Continuation — EUL/USDT P89_100

**Symbol:** EUL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 147 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7524 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -2.4656 |
| sortino_ratio | -0.4265 |
| max_drawdown | 0.3870 |
| cagr | -0.1771 |
| net_avg_win | 63.3767 |
| net_avg_loss | -93.6080 |
| avg_hold_time_bars | 5.7959 |
| exposure | 0.0387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
