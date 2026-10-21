# EMA Hourly Continuation — JUP/USDT P100_200

**Symbol:** JUP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.7687 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.2297 |
| sortino_ratio | -0.2784 |
| max_drawdown | 0.3273 |
| cagr | -0.1207 |
| net_avg_win | 74.5779 |
| net_avg_loss | -93.2281 |
| avg_hold_time_bars | 12.6215 |
| exposure | 0.1440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
