# EMA Hourly Continuation — YGG/USDT P8_55

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.8157 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 1.0058 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -1.9882 |
| sortino_ratio | -0.7628 |
| max_drawdown | 0.6257 |
| cagr | -0.2973 |
| net_avg_win | 72.6434 |
| net_avg_loss | -87.8366 |
| avg_hold_time_bars | 14.2268 |
| exposure | 0.4655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
