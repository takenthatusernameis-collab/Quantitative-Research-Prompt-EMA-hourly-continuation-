# EMA Hourly Continuation — IO/USDT P55_89

**Symbol:** IO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.4555 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.7291 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -6.0764 |
| sortino_ratio | -2.2529 |
| max_drawdown | 0.9244 |
| cagr | -0.6579 |
| net_avg_win | 27.8991 |
| net_avg_loss | -46.3098 |
| avg_hold_time_bars | 3.6037 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
