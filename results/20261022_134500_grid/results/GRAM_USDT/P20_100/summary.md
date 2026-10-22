# EMA Hourly Continuation — GRAM/USDT P20_100

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.4499 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8692 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -6.3778 |
| sortino_ratio | -2.3982 |
| max_drawdown | 0.9533 |
| cagr | -0.6962 |
| net_avg_win | 24.2040 |
| net_avg_loss | -42.9546 |
| avg_hold_time_bars | 12.3071 |
| exposure | 0.4045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
