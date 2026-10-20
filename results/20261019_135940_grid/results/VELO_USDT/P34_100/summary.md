# EMA Hourly Continuation — VELO/USDT P34_100

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.6927 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9865 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -3.0177 |
| sortino_ratio | -1.1122 |
| max_drawdown | 0.7476 |
| cagr | -0.4071 |
| net_avg_win | 49.4902 |
| net_avg_loss | -69.5604 |
| avg_hold_time_bars | 8.5541 |
| exposure | 0.2625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
