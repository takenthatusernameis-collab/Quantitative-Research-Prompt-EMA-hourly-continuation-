# EMA Hourly Continuation — THETA/USDT P26_34

**Symbol:** THETA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1036 |
| net_profit_factor | 0.2700 |
| net_win_rate | 0.3697 |
| gross_profit_factor | 0.6788 |
| gross_win_rate | 0.4044 |
| sharpe_ratio | -12.6532 |
| sortino_ratio | -5.8821 |
| max_drawdown | 0.9996 |
| cagr | -0.9543 |
| net_avg_win | 9.6521 |
| net_avg_loss | -20.9685 |
| avg_hold_time_bars | 2.0222 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
