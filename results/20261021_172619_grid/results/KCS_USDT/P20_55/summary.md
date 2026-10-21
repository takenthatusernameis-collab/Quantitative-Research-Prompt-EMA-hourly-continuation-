# EMA Hourly Continuation — KCS/USDT P20_55

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.3787 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.7152 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -6.6043 |
| sortino_ratio | -2.1009 |
| max_drawdown | 0.9178 |
| cagr | -0.6289 |
| net_avg_win | 28.2299 |
| net_avg_loss | -51.6081 |
| avg_hold_time_bars | 9.8636 |
| exposure | 0.2170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
