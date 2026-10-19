# EMA Hourly Continuation — JASMY/USDT P26_34

**Symbol:** JASMY/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.2344 |
| net_win_rate | 0.3617 |
| gross_profit_factor | 0.5491 |
| gross_win_rate | 0.3911 |
| sharpe_ratio | -13.1766 |
| sortino_ratio | -6.2033 |
| max_drawdown | 0.9997 |
| cagr | -0.9617 |
| net_avg_win | 8.0135 |
| net_avg_loss | -19.3744 |
| avg_hold_time_bars | 1.7917 |
| exposure | 0.0860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
