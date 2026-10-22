# EMA Hourly Continuation — ALPINE/USDT P12_34

**Symbol:** ALPINE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.4274 |
| net_win_rate | 0.4093 |
| gross_profit_factor | 0.7660 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -9.5269 |
| sortino_ratio | -4.4651 |
| max_drawdown | 0.9960 |
| cagr | -0.8891 |
| net_avg_win | 16.5573 |
| net_avg_loss | -26.8430 |
| avg_hold_time_bars | 5.5169 |
| exposure | 0.2751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
