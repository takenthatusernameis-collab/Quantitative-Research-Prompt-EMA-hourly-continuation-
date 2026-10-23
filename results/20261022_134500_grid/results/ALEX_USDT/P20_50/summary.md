# EMA Hourly Continuation — ALEX/USDT P20_50

**Symbol:** ALEX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 838 |
| net_profit_factor | 0.4986 |
| net_win_rate | 0.3842 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4069 |
| sharpe_ratio | -8.3638 |
| sortino_ratio | -3.3918 |
| max_drawdown | 0.9868 |
| cagr | -0.8179 |
| net_avg_win | 30.4528 |
| net_avg_loss | -38.1142 |
| avg_hold_time_bars | 7.5322 |
| exposure | 0.2869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
