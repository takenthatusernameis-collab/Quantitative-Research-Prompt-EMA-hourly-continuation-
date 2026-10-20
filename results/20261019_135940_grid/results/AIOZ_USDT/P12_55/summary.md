# EMA Hourly Continuation — AIOZ/USDT P12_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1162 |
| net_profit_factor | 0.6707 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.9850 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -6.0851 |
| sortino_ratio | -2.9218 |
| max_drawdown | 0.9710 |
| cagr | -0.7529 |
| net_avg_win | 36.6656 |
| net_avg_loss | -47.2938 |
| avg_hold_time_bars | 7.1377 |
| exposure | 0.3770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
