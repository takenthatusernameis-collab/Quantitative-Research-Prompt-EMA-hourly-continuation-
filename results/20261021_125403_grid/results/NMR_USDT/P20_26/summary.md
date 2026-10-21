# EMA Hourly Continuation — NMR/USDT P20_26

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7479 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.1471 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -1.8384 |
| sortino_ratio | -0.4670 |
| max_drawdown | 0.5001 |
| cagr | -0.1921 |
| net_avg_win | 75.9610 |
| net_avg_loss | -111.1687 |
| avg_hold_time_bars | 5.0839 |
| exposure | 0.0716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
