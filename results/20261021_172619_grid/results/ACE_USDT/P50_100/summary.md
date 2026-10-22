# EMA Hourly Continuation — ACE/USDT P50_100

**Symbol:** ACE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9811 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.8600 |
| sortino_ratio | -0.5139 |
| max_drawdown | 0.4673 |
| cagr | -0.2101 |
| net_avg_win | 67.9718 |
| net_avg_loss | -90.2584 |
| avg_hold_time_bars | 10.4893 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
