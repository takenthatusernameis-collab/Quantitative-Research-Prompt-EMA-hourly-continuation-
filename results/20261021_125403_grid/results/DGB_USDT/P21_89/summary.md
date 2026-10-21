# EMA Hourly Continuation — DGB/USDT P21_89

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7708 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -1.8416 |
| sortino_ratio | -0.5948 |
| max_drawdown | 0.5067 |
| cagr | -0.2397 |
| net_avg_win | 66.4128 |
| net_avg_loss | -84.1540 |
| avg_hold_time_bars | 14.2529 |
| exposure | 0.3304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
