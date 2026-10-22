# EMA Hourly Continuation — AXS/USDT P100_200

**Symbol:** AXS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6724 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0932 |
| gross_win_rate | 0.5288 |
| sharpe_ratio | -2.2936 |
| sortino_ratio | -0.6324 |
| max_drawdown | 0.5502 |
| cagr | -0.2613 |
| net_avg_win | 55.3711 |
| net_avg_loss | -88.6170 |
| avg_hold_time_bars | 7.9476 |
| exposure | 0.1374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
