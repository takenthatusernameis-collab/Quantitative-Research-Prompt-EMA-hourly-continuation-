# EMA Hourly Continuation — MEME/USDT P20_50

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -3.2779 |
| sortino_ratio | -1.1277 |
| max_drawdown | 0.7547 |
| cagr | -0.4035 |
| net_avg_win | 56.2449 |
| net_avg_loss | -72.3809 |
| avg_hold_time_bars | 6.8402 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
