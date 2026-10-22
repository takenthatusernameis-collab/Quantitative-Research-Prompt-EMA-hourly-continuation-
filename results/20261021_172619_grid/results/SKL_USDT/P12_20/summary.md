# EMA Hourly Continuation — SKL/USDT P12_20

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -2.5465 |
| sortino_ratio | -0.6909 |
| max_drawdown | 0.5626 |
| cagr | -0.2705 |
| net_avg_win | 61.3435 |
| net_avg_loss | -86.9404 |
| avg_hold_time_bars | 4.2486 |
| exposure | 0.0691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
