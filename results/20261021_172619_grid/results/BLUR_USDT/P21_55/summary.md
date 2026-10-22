# EMA Hourly Continuation — BLUR/USDT P21_55

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.7184 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -2.5485 |
| sortino_ratio | -0.8735 |
| max_drawdown | 0.6755 |
| cagr | -0.3302 |
| net_avg_win | 57.5605 |
| net_avg_loss | -76.5889 |
| avg_hold_time_bars | 7.7244 |
| exposure | 0.2017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
