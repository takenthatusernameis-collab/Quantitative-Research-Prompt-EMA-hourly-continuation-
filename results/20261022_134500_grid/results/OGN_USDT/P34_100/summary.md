# EMA Hourly Continuation — OGN/USDT P34_100

**Symbol:** OGN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.4965 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.8577 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -5.9682 |
| sortino_ratio | -2.1410 |
| max_drawdown | 0.9348 |
| cagr | -0.6533 |
| net_avg_win | 31.8734 |
| net_avg_loss | -49.5667 |
| avg_hold_time_bars | 9.8956 |
| exposure | 0.2960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
