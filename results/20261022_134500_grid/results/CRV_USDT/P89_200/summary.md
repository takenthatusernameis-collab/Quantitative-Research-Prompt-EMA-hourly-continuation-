# EMA Hourly Continuation — CRV/USDT P89_200

**Symbol:** CRV/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.5528 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.8634 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -3.9476 |
| sortino_ratio | -1.1873 |
| max_drawdown | 0.7691 |
| cagr | -0.4353 |
| net_avg_win | 44.6366 |
| net_avg_loss | -69.2584 |
| avg_hold_time_bars | 7.9628 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
