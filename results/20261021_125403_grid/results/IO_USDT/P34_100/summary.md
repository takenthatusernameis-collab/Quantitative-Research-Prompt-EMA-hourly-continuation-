# EMA Hourly Continuation — IO/USDT P34_100

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.4849 |
| gross_profit_factor | 0.9349 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -1.5957 |
| sortino_ratio | -0.4690 |
| max_drawdown | 0.4220 |
| cagr | -0.1946 |
| net_avg_win | 72.3278 |
| net_avg_loss | -87.5930 |
| avg_hold_time_bars | 10.9724 |
| exposure | 0.2114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
