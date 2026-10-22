# EMA Hourly Continuation — FLIP/USDT P50_144

**Symbol:** FLIP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.5587 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.7558 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -3.1469 |
| sortino_ratio | -0.7114 |
| max_drawdown | 0.5896 |
| cagr | -0.2874 |
| net_avg_win | 65.9412 |
| net_avg_loss | -86.5507 |
| avg_hold_time_bars | 23.2154 |
| exposure | 0.2744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
