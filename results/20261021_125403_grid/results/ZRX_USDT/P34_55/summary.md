# EMA Hourly Continuation — ZRX/USDT P34_55

**Symbol:** ZRX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.5827 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8663 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -3.8610 |
| sortino_ratio | -1.2075 |
| max_drawdown | 0.7553 |
| cagr | -0.4249 |
| net_avg_win | 47.6511 |
| net_avg_loss | -70.2773 |
| avg_hold_time_bars | 5.8130 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
