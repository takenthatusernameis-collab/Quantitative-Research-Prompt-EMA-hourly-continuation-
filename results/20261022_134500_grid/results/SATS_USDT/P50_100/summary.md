# EMA Hourly Continuation — SATS/USDT P50_100

**Symbol:** SATS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.5336 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8318 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -4.4630 |
| sortino_ratio | -1.4896 |
| max_drawdown | 0.8350 |
| cagr | -0.5080 |
| net_avg_win | 37.9633 |
| net_avg_loss | -56.8714 |
| avg_hold_time_bars | 6.9257 |
| exposure | 0.1771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
