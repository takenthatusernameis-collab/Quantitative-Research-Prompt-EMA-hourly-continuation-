# EMA Hourly Continuation — NMR/USDT P55_200

**Symbol:** NMR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8663 |
| net_win_rate | 0.5292 |
| gross_profit_factor | 1.1057 |
| gross_win_rate | 0.5292 |
| sharpe_ratio | -0.7301 |
| sortino_ratio | -0.1896 |
| max_drawdown | 0.2712 |
| cagr | -0.0859 |
| net_avg_win | 76.0823 |
| net_avg_loss | -98.7251 |
| avg_hold_time_bars | 23.0492 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
