# EMA Hourly Continuation — AIOZ/USDT P12_20

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1583 |
| net_profit_factor | 0.3752 |
| net_win_rate | 0.3917 |
| gross_profit_factor | 0.8101 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -13.8044 |
| sortino_ratio | -7.7610 |
| max_drawdown | 1.0000 |
| cagr | -0.9819 |
| net_avg_win | 9.6864 |
| net_avg_loss | -16.6201 |
| avg_hold_time_bars | 2.1276 |
| exposure | 0.1531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
