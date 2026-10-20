# EMA Hourly Continuation — FIDA/USDT P34_200

**Symbol:** FIDA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8696 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -3.0115 |
| sortino_ratio | -0.8459 |
| max_drawdown | 0.6511 |
| cagr | -0.3339 |
| net_avg_win | 52.1344 |
| net_avg_loss | -74.2373 |
| avg_hold_time_bars | 28.5558 |
| exposure | 0.5207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
