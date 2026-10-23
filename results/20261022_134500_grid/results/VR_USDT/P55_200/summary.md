# EMA Hourly Continuation — VR/USDT P55_200

**Symbol:** VR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.4106 |
| net_win_rate | 0.3158 |
| gross_profit_factor | 0.6034 |
| gross_win_rate | 0.3216 |
| sharpe_ratio | -8.9277 |
| sortino_ratio | -2.8246 |
| max_drawdown | 0.9818 |
| cagr | -0.7961 |
| net_avg_win | 42.2054 |
| net_avg_loss | -47.4438 |
| avg_hold_time_bars | 13.4074 |
| exposure | 0.3126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
