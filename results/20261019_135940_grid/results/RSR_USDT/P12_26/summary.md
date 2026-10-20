# EMA Hourly Continuation — RSR/USDT P12_26

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1371 |
| net_profit_factor | 0.5025 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.9571 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -9.1044 |
| sortino_ratio | -4.7607 |
| max_drawdown | 0.9973 |
| cagr | -0.9043 |
| net_avg_win | 16.2970 |
| net_avg_loss | -26.6188 |
| avg_hold_time_bars | 2.9643 |
| exposure | 0.1847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
