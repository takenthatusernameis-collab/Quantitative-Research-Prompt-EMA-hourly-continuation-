# EMA Hourly Continuation — LUNC/USDT P34_50

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 993 |
| net_profit_factor | 0.2525 |
| net_win_rate | 0.3948 |
| gross_profit_factor | 0.6909 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -11.4851 |
| sortino_ratio | -5.2116 |
| max_drawdown | 0.9988 |
| cagr | -0.9309 |
| net_avg_win | 8.6072 |
| net_avg_loss | -22.2327 |
| avg_hold_time_bars | 2.4804 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
