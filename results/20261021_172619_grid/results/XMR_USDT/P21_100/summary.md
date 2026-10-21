# EMA Hourly Continuation — XMR/USDT P21_100

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6935 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9150 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -2.7055 |
| sortino_ratio | -0.8744 |
| max_drawdown | 0.6479 |
| cagr | -0.3299 |
| net_avg_win | 59.0374 |
| net_avg_loss | -76.3367 |
| avg_hold_time_bars | 12.7490 |
| exposure | 0.2979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
