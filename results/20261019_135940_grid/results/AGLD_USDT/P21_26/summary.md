# EMA Hourly Continuation — AGLD/USDT P21_26

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1158 |
| net_profit_factor | 0.3035 |
| net_win_rate | 0.3800 |
| gross_profit_factor | 0.8261 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -12.2459 |
| sortino_ratio | -5.9496 |
| max_drawdown | 0.9996 |
| cagr | -0.9532 |
| net_avg_win | 9.8971 |
| net_avg_loss | -19.9865 |
| avg_hold_time_bars | 2.7168 |
| exposure | 0.1424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
