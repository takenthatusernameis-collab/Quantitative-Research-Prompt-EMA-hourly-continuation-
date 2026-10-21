# EMA Hourly Continuation — LUNC/USDT P26_34

**Symbol:** LUNC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 170 |
| net_profit_factor | 0.5179 |
| net_win_rate | 0.4176 |
| gross_profit_factor | 0.7296 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -2.7207 |
| sortino_ratio | -0.5058 |
| max_drawdown | 0.4594 |
| cagr | -0.2089 |
| net_avg_win | 67.3137 |
| net_avg_loss | -93.2088 |
| avg_hold_time_bars | 4.2882 |
| exposure | 0.0331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
