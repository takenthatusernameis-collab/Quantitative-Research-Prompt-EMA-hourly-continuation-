# EMA Hourly Continuation — TAO/USDT P12_34

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7286 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.5811 |
| sortino_ratio | -0.8488 |
| max_drawdown | 0.6475 |
| cagr | -0.3240 |
| net_avg_win | 67.2210 |
| net_avg_loss | -81.4997 |
| avg_hold_time_bars | 6.8630 |
| exposure | 0.1663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
