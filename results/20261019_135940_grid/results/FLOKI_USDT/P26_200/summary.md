# EMA Hourly Continuation — FLOKI/USDT P26_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.6108 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8282 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -2.9200 |
| sortino_ratio | -0.7573 |
| max_drawdown | 0.6045 |
| cagr | -0.3021 |
| net_avg_win | 61.0046 |
| net_avg_loss | -82.1610 |
| avg_hold_time_bars | 40.8820 |
| exposure | 0.6300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
