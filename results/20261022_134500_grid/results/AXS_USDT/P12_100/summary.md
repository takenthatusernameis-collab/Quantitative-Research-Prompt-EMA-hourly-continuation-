# EMA Hourly Continuation — AXS/USDT P12_100

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 1.0237 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -3.2777 |
| sortino_ratio | -1.1587 |
| max_drawdown | 0.7684 |
| cagr | -0.4292 |
| net_avg_win | 52.1173 |
| net_avg_loss | -73.8715 |
| avg_hold_time_bars | 19.2759 |
| exposure | 0.5565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
