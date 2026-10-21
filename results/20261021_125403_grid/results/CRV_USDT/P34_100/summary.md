# EMA Hourly Continuation — CRV/USDT P34_100

**Symbol:** CRV/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.8101 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0077 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.4493 |
| sortino_ratio | -0.4249 |
| max_drawdown | 0.4358 |
| cagr | -0.1784 |
| net_avg_win | 79.5198 |
| net_avg_loss | -97.6874 |
| avg_hold_time_bars | 12.2076 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
