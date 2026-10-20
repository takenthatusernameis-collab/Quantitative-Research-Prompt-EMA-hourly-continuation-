# EMA Hourly Continuation — BLUR/USDT P21_100

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.6655 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 1.0208 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -3.5964 |
| sortino_ratio | -1.2527 |
| max_drawdown | 0.8045 |
| cagr | -0.4541 |
| net_avg_win | 52.2622 |
| net_avg_loss | -73.8238 |
| avg_hold_time_bars | 16.3480 |
| exposure | 0.4550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
