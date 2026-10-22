# EMA Hourly Continuation — SSV/USDT P26_50

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7791 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0533 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.7519 |
| sortino_ratio | -0.5401 |
| max_drawdown | 0.4823 |
| cagr | -0.2200 |
| net_avg_win | 69.5912 |
| net_avg_loss | -93.2763 |
| avg_hold_time_bars | 6.6429 |
| exposure | 0.1389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
