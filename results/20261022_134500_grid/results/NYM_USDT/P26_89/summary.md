# EMA Hourly Continuation — NYM/USDT P26_89

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.2977 |
| net_win_rate | 0.3557 |
| gross_profit_factor | 0.6349 |
| gross_win_rate | 0.3934 |
| sharpe_ratio | -8.8562 |
| sortino_ratio | -3.0882 |
| max_drawdown | 0.9841 |
| cagr | -0.8037 |
| net_avg_win | 19.2055 |
| net_avg_loss | -35.6233 |
| avg_hold_time_bars | 12.2492 |
| exposure | 0.3396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
