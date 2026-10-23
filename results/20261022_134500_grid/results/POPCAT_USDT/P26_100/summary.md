# EMA Hourly Continuation — POPCAT/USDT P26_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.5978 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8160 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -4.6995 |
| sortino_ratio | -1.7132 |
| max_drawdown | 0.8358 |
| cagr | -0.5666 |
| net_avg_win | 47.7684 |
| net_avg_loss | -63.1536 |
| avg_hold_time_bars | 11.7810 |
| exposure | 0.3666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
