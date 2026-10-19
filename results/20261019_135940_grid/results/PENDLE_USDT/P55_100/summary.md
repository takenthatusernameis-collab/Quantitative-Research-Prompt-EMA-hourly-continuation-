# EMA Hourly Continuation — PENDLE/USDT P55_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.5884 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -4.3605 |
| sortino_ratio | -1.5769 |
| max_drawdown | 0.8540 |
| cagr | -0.5301 |
| net_avg_win | 38.9446 |
| net_avg_loss | -60.3805 |
| avg_hold_time_bars | 4.7232 |
| exposure | 0.1404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
