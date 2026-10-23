# EMA Hourly Continuation — CETUS/USDT P20_21

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1224 |
| net_profit_factor | 0.2110 |
| net_win_rate | 0.3154 |
| gross_profit_factor | 0.8218 |
| gross_win_rate | 0.3889 |
| sharpe_ratio | -16.5408 |
| sortino_ratio | -8.5542 |
| max_drawdown | 1.0000 |
| cagr | -0.9915 |
| net_avg_win | 6.9278 |
| net_avg_loss | -15.1242 |
| avg_hold_time_bars | 1.7917 |
| exposure | 0.0992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
