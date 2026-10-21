# EMA Hourly Continuation — METIS/USDT P34_50

**Symbol:** METIS/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7031 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -2.0017 |
| sortino_ratio | -0.5165 |
| max_drawdown | 0.4653 |
| cagr | -0.2106 |
| net_avg_win | 65.8674 |
| net_avg_loss | -93.1008 |
| avg_hold_time_bars | 5.2817 |
| exposure | 0.0775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
