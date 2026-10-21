# EMA Hourly Continuation — WAVES/USDT P21_50

**Symbol:** WAVES/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.5672 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8190 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -4.4574 |
| sortino_ratio | -1.4354 |
| max_drawdown | 0.8136 |
| cagr | -0.4863 |
| net_avg_win | 47.5288 |
| net_avg_loss | -65.6267 |
| avg_hold_time_bars | 7.2980 |
| exposure | 0.1692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
