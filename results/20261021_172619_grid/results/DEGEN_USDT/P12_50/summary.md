# EMA Hourly Continuation — DEGEN/USDT P12_50

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.8257 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.7511 |
| sortino_ratio | -0.6148 |
| max_drawdown | 0.5576 |
| cagr | -0.2485 |
| net_avg_win | 81.8230 |
| net_avg_loss | -95.2396 |
| avg_hold_time_bars | 11.6937 |
| exposure | 0.3216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
