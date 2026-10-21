# EMA Hourly Continuation — BAND/USDT P144_200

**Symbol:** BAND/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.7122 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0381 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.6580 |
| sortino_ratio | -0.3862 |
| max_drawdown | 0.4007 |
| cagr | -0.1621 |
| net_avg_win | 65.9765 |
| net_avg_loss | -97.6987 |
| avg_hold_time_bars | 6.1217 |
| exposure | 0.0729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
