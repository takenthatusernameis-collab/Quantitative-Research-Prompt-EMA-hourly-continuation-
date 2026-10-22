# EMA Hourly Continuation — SKY/USDT P21_89

**Symbol:** SKY/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6334 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9884 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -4.1504 |
| sortino_ratio | -1.4905 |
| max_drawdown | 0.8138 |
| cagr | -0.5150 |
| net_avg_win | 52.5494 |
| net_avg_loss | -74.9960 |
| avg_hold_time_bars | 14.3944 |
| exposure | 0.4294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
