# EMA Hourly Continuation — SSV/USDT P8_26

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.7785 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -2.8132 |
| sortino_ratio | -1.0989 |
| max_drawdown | 0.7535 |
| cagr | -0.3957 |
| net_avg_win | 69.2729 |
| net_avg_loss | -84.5769 |
| avg_hold_time_bars | 7.2897 |
| exposure | 0.2471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
