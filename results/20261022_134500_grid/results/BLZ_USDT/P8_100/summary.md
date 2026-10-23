# EMA Hourly Continuation — BLZ/USDT P8_100

**Symbol:** BLZ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.5688 |
| net_win_rate | 0.4156 |
| gross_profit_factor | 0.8088 |
| gross_win_rate | 0.4213 |
| sharpe_ratio | -5.7696 |
| sortino_ratio | -2.1414 |
| max_drawdown | 0.9290 |
| cagr | -0.6419 |
| net_avg_win | 41.6501 |
| net_avg_loss | -52.0711 |
| avg_hold_time_bars | 20.6340 |
| exposure | 0.6583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
