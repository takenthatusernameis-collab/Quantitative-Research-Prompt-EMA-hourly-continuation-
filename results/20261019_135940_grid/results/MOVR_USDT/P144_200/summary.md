# EMA Hourly Continuation — MOVR/USDT P144_200

**Symbol:** MOVR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.4028 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.7153 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -5.0619 |
| sortino_ratio | -1.5390 |
| max_drawdown | 0.8523 |
| cagr | -0.5251 |
| net_avg_win | 28.3873 |
| net_avg_loss | -54.9029 |
| avg_hold_time_bars | 4.8715 |
| exposure | 0.1016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
