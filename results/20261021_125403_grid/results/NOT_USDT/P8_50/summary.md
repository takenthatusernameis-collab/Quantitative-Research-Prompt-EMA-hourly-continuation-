# EMA Hourly Continuation — NOT/USDT P8_50

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.8600 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0489 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.1341 |
| sortino_ratio | -0.4111 |
| max_drawdown | 0.4757 |
| cagr | -0.1758 |
| net_avg_win | 72.6791 |
| net_avg_loss | -89.8940 |
| avg_hold_time_bars | 14.2211 |
| exposure | 0.4108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
