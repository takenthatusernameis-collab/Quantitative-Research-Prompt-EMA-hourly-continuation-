# EMA Hourly Continuation — EGLD/USDT P20_26

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1205 |
| net_profit_factor | 0.2222 |
| net_win_rate | 0.3718 |
| gross_profit_factor | 0.7536 |
| gross_win_rate | 0.4324 |
| sharpe_ratio | -14.1041 |
| sortino_ratio | -7.1273 |
| max_drawdown | 0.9999 |
| cagr | -0.9771 |
| net_avg_win | 6.3772 |
| net_avg_loss | -16.9831 |
| avg_hold_time_bars | 2.0373 |
| exposure | 0.1116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
