# EMA Hourly Continuation — SLP/USDT P12_100

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.7632 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9393 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -2.1056 |
| sortino_ratio | -0.6910 |
| max_drawdown | 0.5747 |
| cagr | -0.2735 |
| net_avg_win | 69.7512 |
| net_avg_loss | -84.7419 |
| avg_hold_time_bars | 22.8962 |
| exposure | 0.5516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
