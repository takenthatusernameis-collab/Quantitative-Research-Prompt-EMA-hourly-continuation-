# EMA Hourly Continuation — LQTY/USDT P26_34

**Symbol:** LQTY/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.6914 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0337 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -1.9071 |
| sortino_ratio | -0.4546 |
| max_drawdown | 0.4199 |
| cagr | -0.1872 |
| net_avg_win | 65.1682 |
| net_avg_loss | -97.7421 |
| avg_hold_time_bars | 5.2327 |
| exposure | 0.0651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
