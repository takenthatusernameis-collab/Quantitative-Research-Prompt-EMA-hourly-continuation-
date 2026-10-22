# EMA Hourly Continuation — IOTX/USDT P8_21

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6968 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9931 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.7303 |
| sortino_ratio | -0.9566 |
| max_drawdown | 0.6730 |
| cagr | -0.3533 |
| net_avg_win | 51.4805 |
| net_avg_loss | -73.8800 |
| avg_hold_time_bars | 5.3131 |
| exposure | 0.1435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
