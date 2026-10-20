# EMA Hourly Continuation — MINA/USDT P12_26

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1410 |
| net_profit_factor | 0.3392 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.7543 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -10.9352 |
| sortino_ratio | -5.8395 |
| max_drawdown | 0.9993 |
| cagr | -0.9440 |
| net_avg_win | 8.5925 |
| net_avg_loss | -18.6009 |
| avg_hold_time_bars | 3.1858 |
| exposure | 0.2042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
