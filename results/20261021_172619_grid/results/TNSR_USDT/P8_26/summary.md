# EMA Hourly Continuation — TNSR/USDT P8_26

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.7999 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 1.0481 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -2.5149 |
| sortino_ratio | -0.9920 |
| max_drawdown | 0.7337 |
| cagr | -0.3660 |
| net_avg_win | 71.6878 |
| net_avg_loss | -89.8557 |
| avg_hold_time_bars | 6.1064 |
| exposure | 0.2103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
