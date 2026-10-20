# EMA Hourly Continuation — IOST/USDT P26_50

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.3972 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.8300 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -8.3707 |
| sortino_ratio | -3.6132 |
| max_drawdown | 0.9890 |
| cagr | -0.8327 |
| net_avg_win | 16.2090 |
| net_avg_loss | -31.3049 |
| avg_hold_time_bars | 4.4136 |
| exposure | 0.1858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
