# EMA Hourly Continuation — ORCA/USDT P55_100

**Symbol:** ORCA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.5349 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8874 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -4.6069 |
| sortino_ratio | -1.5690 |
| max_drawdown | 0.8547 |
| cagr | -0.5290 |
| net_avg_win | 36.0283 |
| net_avg_loss | -58.3199 |
| avg_hold_time_bars | 6.2089 |
| exposure | 0.1648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
