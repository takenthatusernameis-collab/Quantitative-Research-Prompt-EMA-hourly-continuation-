# EMA Hourly Continuation — ANYONE/USDT P26_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7617 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8636 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -1.5906 |
| sortino_ratio | -0.4146 |
| max_drawdown | 0.4030 |
| cagr | -0.1751 |
| net_avg_win | 79.9362 |
| net_avg_loss | -90.7823 |
| avg_hold_time_bars | 31.1480 |
| exposure | 0.4785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
