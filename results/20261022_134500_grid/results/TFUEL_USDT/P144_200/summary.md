# EMA Hourly Continuation — TFUEL/USDT P144_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.3802 |
| net_win_rate | 0.3868 |
| gross_profit_factor | 0.7974 |
| gross_win_rate | 0.4115 |
| sharpe_ratio | -7.3777 |
| sortino_ratio | -2.3305 |
| max_drawdown | 0.9495 |
| cagr | -0.6917 |
| net_avg_win | 30.9501 |
| net_avg_loss | -51.3580 |
| avg_hold_time_bars | 4.3292 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
