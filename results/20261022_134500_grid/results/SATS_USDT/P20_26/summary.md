# EMA Hourly Continuation — SATS/USDT P20_26

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.3461 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -9.0887 |
| sortino_ratio | -3.8817 |
| max_drawdown | 0.9933 |
| cagr | -0.8617 |
| net_avg_win | 13.6210 |
| net_avg_loss | -28.4986 |
| avg_hold_time_bars | 2.4233 |
| exposure | 0.1008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
