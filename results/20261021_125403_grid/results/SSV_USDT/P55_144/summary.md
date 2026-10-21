# EMA Hourly Continuation — SSV/USDT P55_144

**Symbol:** SSV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7025 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8746 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -2.2080 |
| sortino_ratio | -0.6029 |
| max_drawdown | 0.5220 |
| cagr | -0.2416 |
| net_avg_win | 68.5483 |
| net_avg_loss | -85.2582 |
| avg_hold_time_bars | 14.8005 |
| exposure | 0.2485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
