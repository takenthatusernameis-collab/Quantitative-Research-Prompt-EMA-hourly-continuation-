# EMA Hourly Continuation — ZIL/USDT P26_34

**Symbol:** ZIL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1096 |
| net_profit_factor | 0.2177 |
| net_win_rate | 0.3741 |
| gross_profit_factor | 0.6969 |
| gross_win_rate | 0.4288 |
| sharpe_ratio | -13.1896 |
| sortino_ratio | -6.3669 |
| max_drawdown | 0.9998 |
| cagr | -0.9631 |
| net_avg_win | 6.7853 |
| net_avg_loss | -18.6290 |
| avg_hold_time_bars | 2.0474 |
| exposure | 0.1020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
