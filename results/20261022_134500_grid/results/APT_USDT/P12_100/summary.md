# EMA Hourly Continuation — APT/USDT P12_100

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.6359 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9021 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -3.4435 |
| sortino_ratio | -1.1378 |
| max_drawdown | 0.7660 |
| cagr | -0.4199 |
| net_avg_win | 49.8807 |
| net_avg_loss | -70.1090 |
| avg_hold_time_bars | 24.8409 |
| exposure | 0.6244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
