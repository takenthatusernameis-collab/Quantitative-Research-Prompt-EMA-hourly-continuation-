# EMA Hourly Continuation — RIO/USDT P26_55

**Symbol:** RIO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.4699 |
| net_win_rate | 0.4006 |
| gross_profit_factor | 0.7266 |
| gross_win_rate | 0.4045 |
| sharpe_ratio | -8.3539 |
| sortino_ratio | -3.7690 |
| max_drawdown | 0.9903 |
| cagr | -0.8437 |
| net_avg_win | 21.3503 |
| net_avg_loss | -30.3674 |
| avg_hold_time_bars | 3.8216 |
| exposure | 0.1800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
