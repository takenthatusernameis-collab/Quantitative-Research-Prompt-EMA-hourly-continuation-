# EMA Hourly Continuation — ANKR/USDT P21_100

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6659 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8627 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -3.1926 |
| sortino_ratio | -1.0156 |
| max_drawdown | 0.7020 |
| cagr | -0.3746 |
| net_avg_win | 60.5126 |
| net_avg_loss | -75.8987 |
| avg_hold_time_bars | 19.4511 |
| exposure | 0.4430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
