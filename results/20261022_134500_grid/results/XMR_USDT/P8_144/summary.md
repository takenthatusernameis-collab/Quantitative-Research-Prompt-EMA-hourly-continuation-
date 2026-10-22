# EMA Hourly Continuation — XMR/USDT P8_144

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 879 |
| net_profit_factor | 0.4839 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.8827 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -6.8160 |
| sortino_ratio | -2.8145 |
| max_drawdown | 0.9718 |
| cagr | -0.7567 |
| net_avg_win | 23.5958 |
| net_avg_loss | -38.1755 |
| avg_hold_time_bars | 16.0705 |
| exposure | 0.6421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
