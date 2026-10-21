# EMA Hourly Continuation — ENJ/USDT P12_50

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.7754 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0197 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -2.0183 |
| sortino_ratio | -0.7407 |
| max_drawdown | 0.5993 |
| cagr | -0.2889 |
| net_avg_win | 59.7839 |
| net_avg_loss | -79.0035 |
| avg_hold_time_bars | 9.7705 |
| exposure | 0.2909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
