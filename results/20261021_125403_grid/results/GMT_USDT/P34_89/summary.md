# EMA Hourly Continuation — GMT/USDT P34_89

**Symbol:** GMT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6757 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8791 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -2.7945 |
| sortino_ratio | -0.8414 |
| max_drawdown | 0.6337 |
| cagr | -0.3202 |
| net_avg_win | 62.7910 |
| net_avg_loss | -79.4258 |
| avg_hold_time_bars | 9.9642 |
| exposure | 0.2025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
