# EMA Hourly Continuation — REQ/USDT P20_21

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.3973 |
| net_win_rate | 0.4154 |
| gross_profit_factor | 0.7545 |
| gross_win_rate | 0.4154 |
| sharpe_ratio | -4.8110 |
| sortino_ratio | -1.1253 |
| max_drawdown | 0.7434 |
| cagr | -0.4111 |
| net_avg_win | 44.8920 |
| net_avg_loss | -80.2833 |
| avg_hold_time_bars | 4.3500 |
| exposure | 0.0514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
