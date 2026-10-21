# EMA Hourly Continuation — TRAC/USDT P12_200

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.6912 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4431 |
| sharpe_ratio | -2.3019 |
| sortino_ratio | -0.6023 |
| max_drawdown | 0.5222 |
| cagr | -0.2424 |
| net_avg_win | 73.9076 |
| net_avg_loss | -85.0960 |
| avg_hold_time_bars | 43.4548 |
| exposure | 0.6775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
