# EMA Hourly Continuation — ANKR/USDT P34_55

**Symbol:** ANKR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.4408 |
| net_win_rate | 0.4140 |
| gross_profit_factor | 0.9386 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -9.2544 |
| sortino_ratio | -3.9095 |
| max_drawdown | 0.9930 |
| cagr | -0.8612 |
| net_avg_win | 21.3860 |
| net_avg_loss | -34.2802 |
| avg_hold_time_bars | 4.8394 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
