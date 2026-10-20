# EMA Hourly Continuation — RIO/USDT P34_200

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6279 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8043 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -3.2205 |
| sortino_ratio | -0.9717 |
| max_drawdown | 0.7042 |
| cagr | -0.3650 |
| net_avg_win | 57.0994 |
| net_avg_loss | -71.6029 |
| avg_hold_time_bars | 23.5969 |
| exposure | 0.4918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
