# EMA Hourly Continuation — STRAX/USDT P12_100

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.7125 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9115 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.7452 |
| sortino_ratio | -0.9468 |
| max_drawdown | 0.6971 |
| cagr | -0.3525 |
| net_avg_win | 59.2292 |
| net_avg_loss | -75.2541 |
| avg_hold_time_bars | 19.3739 |
| exposure | 0.5164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
