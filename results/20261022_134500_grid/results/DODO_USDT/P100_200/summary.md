# EMA Hourly Continuation — DODO/USDT P100_200

**Symbol:** DODO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.5177 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.7895 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -4.6776 |
| sortino_ratio | -1.4547 |
| max_drawdown | 0.8245 |
| cagr | -0.4932 |
| net_avg_win | 42.7296 |
| net_avg_loss | -61.1573 |
| avg_hold_time_bars | 8.0207 |
| exposure | 0.1757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
