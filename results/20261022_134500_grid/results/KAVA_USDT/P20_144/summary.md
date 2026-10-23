# EMA Hourly Continuation — KAVA/USDT P20_144

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.5661 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.9021 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -4.5904 |
| sortino_ratio | -1.4655 |
| max_drawdown | 0.8443 |
| cagr | -0.5160 |
| net_avg_win | 45.9617 |
| net_avg_loss | -67.7970 |
| avg_hold_time_bars | 24.1453 |
| exposure | 0.5740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
