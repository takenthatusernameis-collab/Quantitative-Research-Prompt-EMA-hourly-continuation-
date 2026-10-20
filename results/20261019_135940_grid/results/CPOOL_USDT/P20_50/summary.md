# EMA Hourly Continuation — CPOOL/USDT P20_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.5469 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8020 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -6.4349 |
| sortino_ratio | -2.8182 |
| max_drawdown | 0.9710 |
| cagr | -0.7539 |
| net_avg_win | 26.3822 |
| net_avg_loss | -39.0841 |
| avg_hold_time_bars | 4.5474 |
| exposure | 0.2050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
