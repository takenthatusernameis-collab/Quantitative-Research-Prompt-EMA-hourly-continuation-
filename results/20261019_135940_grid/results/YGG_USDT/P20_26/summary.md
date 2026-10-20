# EMA Hourly Continuation — YGG/USDT P20_26

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1219 |
| net_profit_factor | 0.3608 |
| net_win_rate | 0.3847 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4249 |
| sharpe_ratio | -12.6893 |
| sortino_ratio | -6.3390 |
| max_drawdown | 0.9997 |
| cagr | -0.9612 |
| net_avg_win | 12.0322 |
| net_avg_loss | -20.8538 |
| avg_hold_time_bars | 2.0730 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
