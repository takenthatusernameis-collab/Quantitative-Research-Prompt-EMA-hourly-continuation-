# EMA Hourly Continuation — LUNA/USDT P26_200

**Symbol:** LUNA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6098 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8976 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -3.7508 |
| sortino_ratio | -1.1170 |
| max_drawdown | 0.7566 |
| cagr | -0.4193 |
| net_avg_win | 55.9414 |
| net_avg_loss | -77.5698 |
| avg_hold_time_bars | 26.8106 |
| exposure | 0.5533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
