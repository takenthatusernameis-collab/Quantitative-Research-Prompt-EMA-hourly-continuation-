# EMA Hourly Continuation — SUSHI/USDT P12_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.5632 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.7907 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -3.2997 |
| sortino_ratio | -0.8729 |
| max_drawdown | 0.6581 |
| cagr | -0.3443 |
| net_avg_win | 53.1314 |
| net_avg_loss | -74.6245 |
| avg_hold_time_bars | 46.0333 |
| exposure | 0.7499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
