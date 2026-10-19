# EMA Hourly Continuation — FLR/USDT P26_200

**Symbol:** FLR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9762 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -3.6205 |
| sortino_ratio | -1.2241 |
| max_drawdown | 0.7847 |
| cagr | -0.4439 |
| net_avg_win | 45.6346 |
| net_avg_loss | -68.2109 |
| avg_hold_time_bars | 19.1612 |
| exposure | 0.5025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
