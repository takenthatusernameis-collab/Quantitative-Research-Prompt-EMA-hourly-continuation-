# EMA Hourly Continuation — EGLD/USDT P20_26

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.6184 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.1297 |
| sortino_ratio | -0.4363 |
| max_drawdown | 0.4249 |
| cagr | -0.1816 |
| net_avg_win | 65.3951 |
| net_avg_loss | -97.7705 |
| avg_hold_time_bars | 4.8775 |
| exposure | 0.0452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
