# EMA Hourly Continuation — IOTX/USDT P55_89

**Symbol:** IOTX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.4324 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.8302 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -6.9711 |
| sortino_ratio | -2.6090 |
| max_drawdown | 0.9631 |
| cagr | -0.7303 |
| net_avg_win | 23.3627 |
| net_avg_loss | -42.8374 |
| avg_hold_time_bars | 3.9451 |
| exposure | 0.1273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
