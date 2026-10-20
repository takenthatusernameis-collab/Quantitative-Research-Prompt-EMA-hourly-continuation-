# EMA Hourly Continuation — IOTX/USDT P50_200

**Symbol:** IOTX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6529 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9510 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -2.4360 |
| sortino_ratio | -0.7073 |
| max_drawdown | 0.6163 |
| cagr | -0.2866 |
| net_avg_win | 50.9802 |
| net_avg_loss | -75.9219 |
| avg_hold_time_bars | 20.1893 |
| exposure | 0.3928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
