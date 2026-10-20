# EMA Hourly Continuation — AIOZ/USDT P55_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.5873 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -6.0660 |
| sortino_ratio | -2.3871 |
| max_drawdown | 0.9490 |
| cagr | -0.6863 |
| net_avg_win | 38.1166 |
| net_avg_loss | -54.4212 |
| avg_hold_time_bars | 4.0568 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
