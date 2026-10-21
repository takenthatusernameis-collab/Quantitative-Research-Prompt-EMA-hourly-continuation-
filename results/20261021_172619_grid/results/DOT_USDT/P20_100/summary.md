# EMA Hourly Continuation — DOT/USDT P20_100

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.8319 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0511 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.2390 |
| sortino_ratio | -0.3755 |
| max_drawdown | 0.4428 |
| cagr | -0.1603 |
| net_avg_win | 77.0813 |
| net_avg_loss | -97.3516 |
| avg_hold_time_bars | 21.0090 |
| exposure | 0.4250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
