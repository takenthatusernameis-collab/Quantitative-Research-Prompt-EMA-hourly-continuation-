# EMA Hourly Continuation — TWT/USDT P34_200

**Symbol:** TWT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.8282 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0403 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -0.9394 |
| sortino_ratio | -0.2201 |
| max_drawdown | 0.2732 |
| cagr | -0.0976 |
| net_avg_win | 80.6163 |
| net_avg_loss | -101.0517 |
| avg_hold_time_bars | 46.1161 |
| exposure | 0.5597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
