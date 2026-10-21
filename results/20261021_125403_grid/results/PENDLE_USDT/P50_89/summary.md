# EMA Hourly Continuation — PENDLE/USDT P50_89

**Symbol:** PENDLE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7620 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -1.5174 |
| sortino_ratio | -0.4168 |
| max_drawdown | 0.4278 |
| cagr | -0.1745 |
| net_avg_win | 66.8641 |
| net_avg_loss | -87.2750 |
| avg_hold_time_bars | 6.5341 |
| exposure | 0.1090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
