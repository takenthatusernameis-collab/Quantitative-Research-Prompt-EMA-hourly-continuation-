# EMA Hourly Continuation — YGG/USDT P12_26

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1424 |
| net_profit_factor | 0.4796 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -9.9441 |
| sortino_ratio | -5.3013 |
| max_drawdown | 0.9986 |
| cagr | -0.9244 |
| net_avg_win | 14.9657 |
| net_avg_loss | -23.7195 |
| avg_hold_time_bars | 2.9979 |
| exposure | 0.1932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
