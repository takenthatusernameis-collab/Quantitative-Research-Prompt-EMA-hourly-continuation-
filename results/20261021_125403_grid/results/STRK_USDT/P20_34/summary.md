# EMA Hourly Continuation — STRK/USDT P20_34

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.6663 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -2.0602 |
| sortino_ratio | -0.5142 |
| max_drawdown | 0.4554 |
| cagr | -0.2095 |
| net_avg_win | 61.4138 |
| net_avg_loss | -83.5263 |
| avg_hold_time_bars | 5.3311 |
| exposure | 0.0739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
