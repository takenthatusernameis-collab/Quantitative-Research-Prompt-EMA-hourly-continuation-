# EMA Hourly Continuation — STRK/USDT P12_55

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.6131 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9605 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -5.0602 |
| sortino_ratio | -2.2362 |
| max_drawdown | 0.9316 |
| cagr | -0.6554 |
| net_avg_win | 31.4613 |
| net_avg_loss | -47.0051 |
| avg_hold_time_bars | 8.7064 |
| exposure | 0.3882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
