# EMA Hourly Continuation — KMNO/USDT P26_55

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.5252 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8984 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -6.1075 |
| sortino_ratio | -2.4329 |
| max_drawdown | 0.9463 |
| cagr | -0.6910 |
| net_avg_win | 29.7858 |
| net_avg_loss | -46.4023 |
| avg_hold_time_bars | 5.0410 |
| exposure | 0.1815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
