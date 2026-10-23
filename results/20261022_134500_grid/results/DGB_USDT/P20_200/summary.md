# EMA Hourly Continuation — DGB/USDT P20_200

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.7099 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.6803 |
| sortino_ratio | -0.8152 |
| max_drawdown | 0.6609 |
| cagr | -0.3197 |
| net_avg_win | 68.6308 |
| net_avg_loss | -87.9281 |
| avg_hold_time_bars | 29.9289 |
| exposure | 0.6312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
