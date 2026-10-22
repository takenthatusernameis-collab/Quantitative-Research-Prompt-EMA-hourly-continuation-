# EMA Hourly Continuation — LINK/USDT P21_34

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1086 |
| net_profit_factor | 0.3002 |
| net_win_rate | 0.3794 |
| gross_profit_factor | 0.7531 |
| gross_win_rate | 0.4079 |
| sharpe_ratio | -12.4318 |
| sortino_ratio | -5.8678 |
| max_drawdown | 0.9995 |
| cagr | -0.9531 |
| net_avg_win | 10.4059 |
| net_avg_loss | -21.1909 |
| avg_hold_time_bars | 2.5866 |
| exposure | 0.1277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
