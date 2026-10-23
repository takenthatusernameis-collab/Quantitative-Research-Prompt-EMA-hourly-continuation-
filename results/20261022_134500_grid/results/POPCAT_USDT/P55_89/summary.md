# EMA Hourly Continuation — POPCAT/USDT P55_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.4995 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.7533 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -6.0076 |
| sortino_ratio | -2.2884 |
| max_drawdown | 0.9100 |
| cagr | -0.6698 |
| net_avg_win | 33.4638 |
| net_avg_loss | -50.5740 |
| avg_hold_time_bars | 4.3032 |
| exposure | 0.1432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
