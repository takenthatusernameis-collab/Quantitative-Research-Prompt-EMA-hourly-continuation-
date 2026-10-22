# EMA Hourly Continuation — SWFTC/USDT P21_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7672 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.6347 |
| sortino_ratio | -0.4721 |
| max_drawdown | 0.4353 |
| cagr | -0.1957 |
| net_avg_win | 69.4272 |
| net_avg_loss | -86.5952 |
| avg_hold_time_bars | 19.7579 |
| exposure | 0.3673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
