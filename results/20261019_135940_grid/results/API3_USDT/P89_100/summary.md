# EMA Hourly Continuation — API3/USDT P89_100

**Symbol:** API3/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.3425 |
| net_win_rate | 0.3876 |
| gross_profit_factor | 0.8542 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -8.8636 |
| sortino_ratio | -3.1571 |
| max_drawdown | 0.9845 |
| cagr | -0.8078 |
| net_avg_win | 21.5400 |
| net_avg_loss | -39.8075 |
| avg_hold_time_bars | 2.3355 |
| exposure | 0.0652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
