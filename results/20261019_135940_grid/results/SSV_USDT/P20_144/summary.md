# EMA Hourly Continuation — SSV/USDT P20_144

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5813 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8172 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -3.8667 |
| sortino_ratio | -1.1958 |
| max_drawdown | 0.7761 |
| cagr | -0.4334 |
| net_avg_win | 49.3931 |
| net_avg_loss | -67.1019 |
| avg_hold_time_bars | 26.6021 |
| exposure | 0.5838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
