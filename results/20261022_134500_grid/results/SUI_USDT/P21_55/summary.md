# EMA Hourly Continuation — SUI/USDT P21_55

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.5774 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.9574 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -7.1461 |
| sortino_ratio | -3.0920 |
| max_drawdown | 0.9813 |
| cagr | -0.7868 |
| net_avg_win | 31.0437 |
| net_avg_loss | -43.8066 |
| avg_hold_time_bars | 5.2021 |
| exposure | 0.2270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
