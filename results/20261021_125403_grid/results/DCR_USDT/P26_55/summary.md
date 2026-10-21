# EMA Hourly Continuation — DCR/USDT P26_55

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.5410 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.7825 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -3.8666 |
| sortino_ratio | -1.2380 |
| max_drawdown | 0.7732 |
| cagr | -0.4364 |
| net_avg_win | 39.1894 |
| net_avg_loss | -60.1444 |
| avg_hold_time_bars | 6.8619 |
| exposure | 0.1574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
