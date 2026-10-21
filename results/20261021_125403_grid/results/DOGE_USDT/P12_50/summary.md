# EMA Hourly Continuation — DOGE/USDT P12_50

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.7243 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9539 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.5236 |
| sortino_ratio | -0.8836 |
| max_drawdown | 0.6525 |
| cagr | -0.3337 |
| net_avg_win | 57.3066 |
| net_avg_loss | -75.7620 |
| avg_hold_time_bars | 10.2437 |
| exposure | 0.2789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
