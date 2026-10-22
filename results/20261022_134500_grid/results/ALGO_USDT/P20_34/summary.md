# EMA Hourly Continuation — ALGO/USDT P20_34

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1108 |
| net_profit_factor | 0.3518 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -9.6982 |
| sortino_ratio | -4.5791 |
| max_drawdown | 0.9971 |
| cagr | -0.9016 |
| net_avg_win | 11.0199 |
| net_avg_loss | -24.9290 |
| avg_hold_time_bars | 2.5036 |
| exposure | 0.1261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
