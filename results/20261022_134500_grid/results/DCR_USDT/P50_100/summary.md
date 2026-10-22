# EMA Hourly Continuation — DCR/USDT P50_100

**Symbol:** DCR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.4431 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.7795 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -6.3398 |
| sortino_ratio | -2.2844 |
| max_drawdown | 0.9401 |
| cagr | -0.6720 |
| net_avg_win | 26.6153 |
| net_avg_loss | -45.1289 |
| avg_hold_time_bars | 6.6885 |
| exposure | 0.1982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
