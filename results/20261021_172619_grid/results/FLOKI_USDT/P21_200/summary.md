# EMA Hourly Continuation — FLOKI/USDT P21_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.8019 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -1.1323 |
| sortino_ratio | -0.2669 |
| max_drawdown | 0.2964 |
| cagr | -0.1169 |
| net_avg_win | 82.2399 |
| net_avg_loss | -95.3302 |
| avg_hold_time_bars | 52.2774 |
| exposure | 0.6511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
