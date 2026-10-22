# EMA Hourly Continuation — CATI/USDT P20_55

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.6055 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.4324 |
| sharpe_ratio | -3.7657 |
| sortino_ratio | -1.1903 |
| max_drawdown | 0.6955 |
| cagr | -0.4251 |
| net_avg_win | 58.6845 |
| net_avg_loss | -73.8176 |
| avg_hold_time_bars | 10.2198 |
| exposure | 0.2319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
