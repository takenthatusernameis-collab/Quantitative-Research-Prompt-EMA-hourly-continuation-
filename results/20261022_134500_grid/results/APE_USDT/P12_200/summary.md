# EMA Hourly Continuation — APE/USDT P12_200

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6886 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9668 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.8989 |
| sortino_ratio | -0.4616 |
| max_drawdown | 0.4218 |
| cagr | -0.1960 |
| net_avg_win | 63.8726 |
| net_avg_loss | -89.6922 |
| avg_hold_time_bars | 57.6061 |
| exposure | 0.7777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
