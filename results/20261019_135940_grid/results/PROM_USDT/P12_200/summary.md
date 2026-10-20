# EMA Hourly Continuation — PROM/USDT P12_200

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.4804 |
| net_win_rate | 0.4126 |
| gross_profit_factor | 0.7509 |
| gross_win_rate | 0.4368 |
| sharpe_ratio | -5.1076 |
| sortino_ratio | -1.6452 |
| max_drawdown | 0.8766 |
| cagr | -0.5546 |
| net_avg_win | 36.1764 |
| net_avg_loss | -52.9084 |
| avg_hold_time_bars | 27.3680 |
| exposure | 0.6693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
