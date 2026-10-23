# EMA Hourly Continuation — ZPAY/USDT P26_55

**Symbol:** ZPAY/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.3840 |
| net_win_rate | 0.3286 |
| gross_profit_factor | 0.5775 |
| gross_win_rate | 0.3312 |
| sharpe_ratio | -8.6950 |
| sortino_ratio | -3.3818 |
| max_drawdown | 0.9834 |
| cagr | -0.8014 |
| net_avg_win | 24.0356 |
| net_avg_loss | -30.6326 |
| avg_hold_time_bars | 8.6198 |
| exposure | 0.3027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
