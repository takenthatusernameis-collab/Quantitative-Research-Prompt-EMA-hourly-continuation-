# EMA Hourly Continuation — RLC/USDT P21_50

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.5137 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9467 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -6.5124 |
| sortino_ratio | -2.8263 |
| max_drawdown | 0.9705 |
| cagr | -0.7490 |
| net_avg_win | 22.6978 |
| net_avg_loss | -39.7723 |
| avg_hold_time_bars | 4.7279 |
| exposure | 0.2046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
