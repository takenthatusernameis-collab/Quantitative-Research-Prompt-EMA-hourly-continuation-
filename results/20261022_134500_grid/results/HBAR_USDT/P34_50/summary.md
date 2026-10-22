# EMA Hourly Continuation — HBAR/USDT P34_50

**Symbol:** HBAR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 862 |
| net_profit_factor | 0.3231 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.7714 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -9.9368 |
| sortino_ratio | -4.1630 |
| max_drawdown | 0.9955 |
| cagr | -0.8835 |
| net_avg_win | 13.3459 |
| net_avg_loss | -29.0630 |
| avg_hold_time_bars | 2.6253 |
| exposure | 0.1029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
