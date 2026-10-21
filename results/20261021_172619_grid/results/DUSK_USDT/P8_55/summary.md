# EMA Hourly Continuation — DUSK/USDT P8_55

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.8024 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -2.2423 |
| sortino_ratio | -0.8493 |
| max_drawdown | 0.7208 |
| cagr | -0.3248 |
| net_avg_win | 74.8912 |
| net_avg_loss | -86.7028 |
| avg_hold_time_bars | 15.2422 |
| exposure | 0.4891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
