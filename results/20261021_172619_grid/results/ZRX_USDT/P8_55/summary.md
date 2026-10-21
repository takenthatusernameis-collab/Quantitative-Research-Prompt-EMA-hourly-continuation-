# EMA Hourly Continuation — ZRX/USDT P8_55

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 768 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8536 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -3.7391 |
| sortino_ratio | -1.4754 |
| max_drawdown | 0.8274 |
| cagr | -0.4922 |
| net_avg_win | 43.7898 |
| net_avg_loss | -57.9311 |
| avg_hold_time_bars | 13.8646 |
| exposure | 0.4840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
