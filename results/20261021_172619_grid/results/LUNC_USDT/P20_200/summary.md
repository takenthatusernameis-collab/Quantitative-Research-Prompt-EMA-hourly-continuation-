# EMA Hourly Continuation — LUNC/USDT P20_200

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.8183 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0196 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.1450 |
| sortino_ratio | -0.3231 |
| max_drawdown | 0.3715 |
| cagr | -0.1401 |
| net_avg_win | 71.7650 |
| net_avg_loss | -91.3878 |
| avg_hold_time_bars | 31.1598 |
| exposure | 0.5495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
