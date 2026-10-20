# EMA Hourly Continuation — BIGTIME/USDT P12_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1209 |
| net_profit_factor | 0.5924 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9739 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -6.2445 |
| sortino_ratio | -3.0730 |
| max_drawdown | 0.9752 |
| cagr | -0.7670 |
| net_avg_win | 24.3394 |
| net_avg_loss | -38.1370 |
| avg_hold_time_bars | 4.5947 |
| exposure | 0.2514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
