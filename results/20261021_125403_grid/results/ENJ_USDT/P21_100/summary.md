# EMA Hourly Continuation — ENJ/USDT P21_100

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7595 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9561 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.0466 |
| sortino_ratio | -0.6395 |
| max_drawdown | 0.5605 |
| cagr | -0.2548 |
| net_avg_win | 70.9910 |
| net_avg_loss | -87.4667 |
| avg_hold_time_bars | 17.8776 |
| exposure | 0.3899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
