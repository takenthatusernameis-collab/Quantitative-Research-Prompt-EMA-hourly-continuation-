# EMA Hourly Continuation — CPOOL/USDT P26_34

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1004 |
| net_profit_factor | 0.3794 |
| net_win_rate | 0.4094 |
| gross_profit_factor | 0.7229 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -10.0456 |
| sortino_ratio | -4.4931 |
| max_drawdown | 0.9972 |
| cagr | -0.9027 |
| net_avg_win | 14.8310 |
| net_avg_loss | -27.0940 |
| avg_hold_time_bars | 2.1743 |
| exposure | 0.0992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
