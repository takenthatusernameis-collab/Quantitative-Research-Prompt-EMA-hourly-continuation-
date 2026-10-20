# EMA Hourly Continuation — AIOZ/USDT P100_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6189 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9339 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -3.7519 |
| sortino_ratio | -1.1296 |
| max_drawdown | 0.7688 |
| cagr | -0.4182 |
| net_avg_win | 57.2161 |
| net_avg_loss | -79.9445 |
| avg_hold_time_bars | 7.4242 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
