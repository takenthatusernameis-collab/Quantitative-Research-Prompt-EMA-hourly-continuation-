# EMA Hourly Continuation — LISTA/USDT P21_26

**Symbol:** LISTA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.3594 |
| net_win_rate | 0.3725 |
| gross_profit_factor | 0.8306 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -11.8441 |
| sortino_ratio | -5.6033 |
| max_drawdown | 0.9987 |
| cagr | -0.9409 |
| net_avg_win | 14.8643 |
| net_avg_loss | -24.5516 |
| avg_hold_time_bars | 2.6887 |
| exposure | 0.1330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
