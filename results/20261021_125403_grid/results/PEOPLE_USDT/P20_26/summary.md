# EMA Hourly Continuation — PEOPLE/USDT P20_26

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.7525 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0771 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -1.5366 |
| sortino_ratio | -0.3471 |
| max_drawdown | 0.4313 |
| cagr | -0.1468 |
| net_avg_win | 79.0013 |
| net_avg_loss | -111.1050 |
| avg_hold_time_bars | 4.5466 |
| exposure | 0.0508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
