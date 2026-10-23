# EMA Hourly Continuation — TURBO/USDT P21_26

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.3277 |
| net_win_rate | 0.3781 |
| gross_profit_factor | 0.6795 |
| gross_win_rate | 0.4168 |
| sharpe_ratio | -13.3712 |
| sortino_ratio | -6.8464 |
| max_drawdown | 0.9994 |
| cagr | -0.9717 |
| net_avg_win | 12.1791 |
| net_avg_loss | -22.5926 |
| avg_hold_time_bars | 1.8951 |
| exposure | 0.1094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
