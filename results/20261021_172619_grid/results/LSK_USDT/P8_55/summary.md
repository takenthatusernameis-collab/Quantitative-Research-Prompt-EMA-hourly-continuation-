# EMA Hourly Continuation — LSK/USDT P8_55

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.7678 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 1.0313 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -2.6124 |
| sortino_ratio | -0.9987 |
| max_drawdown | 0.7486 |
| cagr | -0.3679 |
| net_avg_win | 63.8757 |
| net_avg_loss | -81.8112 |
| avg_hold_time_bars | 13.8964 |
| exposure | 0.4510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
