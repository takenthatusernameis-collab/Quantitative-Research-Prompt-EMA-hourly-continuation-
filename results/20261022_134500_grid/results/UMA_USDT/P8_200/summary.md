# EMA Hourly Continuation — UMA/USDT P8_200

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.6117 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8709 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -3.3485 |
| sortino_ratio | -1.0842 |
| max_drawdown | 0.7393 |
| cagr | -0.4081 |
| net_avg_win | 45.5837 |
| net_avg_loss | -66.3830 |
| avg_hold_time_bars | 29.7505 |
| exposure | 0.7262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
