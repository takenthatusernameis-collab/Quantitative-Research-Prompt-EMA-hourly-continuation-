# EMA Hourly Continuation — NEAR/USDT P8_50

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1107 |
| net_profit_factor | 0.6172 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -5.0981 |
| sortino_ratio | -2.3924 |
| max_drawdown | 0.9439 |
| cagr | -0.6808 |
| net_avg_win | 28.5341 |
| net_avg_loss | -42.9273 |
| avg_hold_time_bars | 9.1662 |
| exposure | 0.4612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
