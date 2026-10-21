# EMA Hourly Continuation — VR/USDT P89_100

**Symbol:** VR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.4690 |
| net_win_rate | 0.3776 |
| gross_profit_factor | 0.6346 |
| gross_win_rate | 0.3776 |
| sharpe_ratio | -2.4219 |
| sortino_ratio | -0.3373 |
| max_drawdown | 0.3295 |
| cagr | -0.1472 |
| net_avg_win | 78.6644 |
| net_avg_loss | -101.7328 |
| avg_hold_time_bars | 9.5306 |
| exposure | 0.0425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
