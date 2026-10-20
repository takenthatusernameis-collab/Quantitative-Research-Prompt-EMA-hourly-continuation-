# EMA Hourly Continuation — SSV/USDT P12_26

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1478 |
| net_profit_factor | 0.4880 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -10.2687 |
| sortino_ratio | -5.5614 |
| max_drawdown | 0.9990 |
| cagr | -0.9363 |
| net_avg_win | 14.8067 |
| net_avg_loss | -23.3666 |
| avg_hold_time_bars | 3.1604 |
| exposure | 0.2114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
