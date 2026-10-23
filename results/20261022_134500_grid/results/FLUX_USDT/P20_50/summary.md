# EMA Hourly Continuation — FLUX/USDT P20_50

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.5206 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -6.9306 |
| sortino_ratio | -3.1075 |
| max_drawdown | 0.9792 |
| cagr | -0.7855 |
| net_avg_win | 22.3323 |
| net_avg_loss | -37.1289 |
| avg_hold_time_bars | 4.0789 |
| exposure | 0.1902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
