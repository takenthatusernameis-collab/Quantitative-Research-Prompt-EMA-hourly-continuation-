# EMA Hourly Continuation — RUNE/USDT P26_34

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.2909 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.7884 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -11.7214 |
| sortino_ratio | -5.4704 |
| max_drawdown | 0.9993 |
| cagr | -0.9453 |
| net_avg_win | 9.4896 |
| net_avg_loss | -22.2986 |
| avg_hold_time_bars | 1.9784 |
| exposure | 0.0957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
