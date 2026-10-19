# EMA Hourly Continuation — LINK/USDT P26_34

**Symbol:** LINK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.2496 |
| net_win_rate | 0.3607 |
| gross_profit_factor | 0.7460 |
| gross_win_rate | 0.3946 |
| sharpe_ratio | -13.7313 |
| sortino_ratio | -6.4490 |
| max_drawdown | 0.9998 |
| cagr | -0.9680 |
| net_avg_win | 8.9177 |
| net_avg_loss | -20.1581 |
| avg_hold_time_bars | 2.0841 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
