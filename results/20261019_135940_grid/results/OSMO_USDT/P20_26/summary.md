# EMA Hourly Continuation — OSMO/USDT P20_26

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1230 |
| net_profit_factor | 0.2545 |
| net_win_rate | 0.3358 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.3935 |
| sharpe_ratio | -15.3271 |
| sortino_ratio | -7.8339 |
| max_drawdown | 1.0000 |
| cagr | -0.9839 |
| net_avg_win | 8.2662 |
| net_avg_loss | -16.4181 |
| avg_hold_time_bars | 2.4350 |
| exposure | 0.1361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
