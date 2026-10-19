# EMA Hourly Continuation — RAY/USDT P21_89

**Symbol:** RAY/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.5639 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8362 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -5.0359 |
| sortino_ratio | -1.8639 |
| max_drawdown | 0.9036 |
| cagr | -0.5997 |
| net_avg_win | 37.0478 |
| net_avg_loss | -52.8962 |
| avg_hold_time_bars | 10.5611 |
| exposure | 0.3380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
