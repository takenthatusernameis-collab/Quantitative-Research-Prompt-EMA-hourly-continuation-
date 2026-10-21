# EMA Hourly Continuation — FLOKI/USDT P21_55

**Symbol:** FLOKI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.7091 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9004 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -2.6187 |
| sortino_ratio | -0.8389 |
| max_drawdown | 0.6469 |
| cagr | -0.3201 |
| net_avg_win | 63.5612 |
| net_avg_loss | -79.8960 |
| avg_hold_time_bars | 8.5901 |
| exposure | 0.1972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
