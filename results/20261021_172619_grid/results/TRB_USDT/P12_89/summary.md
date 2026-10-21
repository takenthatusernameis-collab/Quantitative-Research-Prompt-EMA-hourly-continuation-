# EMA Hourly Continuation — TRB/USDT P12_89

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6852 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8471 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -2.7737 |
| sortino_ratio | -0.8961 |
| max_drawdown | 0.6599 |
| cagr | -0.3376 |
| net_avg_win | 58.8598 |
| net_avg_loss | -73.0589 |
| avg_hold_time_bars | 21.6596 |
| exposure | 0.5097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
