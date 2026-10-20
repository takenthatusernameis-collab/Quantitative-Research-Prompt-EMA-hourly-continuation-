# EMA Hourly Continuation — ASTR/USDT P21_26

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.2220 |
| net_win_rate | 0.3788 |
| gross_profit_factor | 0.7669 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -13.1842 |
| sortino_ratio | -6.2434 |
| max_drawdown | 0.9998 |
| cagr | -0.9631 |
| net_avg_win | 7.1320 |
| net_avg_loss | -19.5890 |
| avg_hold_time_bars | 2.6061 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
