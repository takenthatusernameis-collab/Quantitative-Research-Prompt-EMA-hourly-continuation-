# EMA Hourly Continuation — FLR/USDT P8_89

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.7562 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9668 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.0754 |
| sortino_ratio | -0.7295 |
| max_drawdown | 0.5912 |
| cagr | -0.2855 |
| net_avg_win | 59.1611 |
| net_avg_loss | -76.6916 |
| avg_hold_time_bars | 20.1738 |
| exposure | 0.5539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
