# EMA Hourly Continuation — SEI/USDT P50_100

**Symbol:** SEI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.5610 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8523 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -5.1019 |
| sortino_ratio | -1.7519 |
| max_drawdown | 0.8822 |
| cagr | -0.5702 |
| net_avg_win | 42.7603 |
| net_avg_loss | -60.9312 |
| avg_hold_time_bars | 6.1976 |
| exposure | 0.1668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
