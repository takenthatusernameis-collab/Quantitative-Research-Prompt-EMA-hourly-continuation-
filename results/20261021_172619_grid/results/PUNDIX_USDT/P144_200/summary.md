# EMA Hourly Continuation — PUNDIX/USDT P144_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.5891 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9309 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.6865 |
| sortino_ratio | -0.6140 |
| max_drawdown | 0.5312 |
| cagr | -0.2467 |
| net_avg_win | 59.8275 |
| net_avg_loss | -93.8564 |
| avg_hold_time_bars | 7.8976 |
| exposure | 0.0912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
