# EMA Hourly Continuation — API3/USDT P8_55

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1042 |
| net_profit_factor | 0.6596 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 1.0068 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -5.1947 |
| sortino_ratio | -2.3404 |
| max_drawdown | 0.9454 |
| cagr | -0.6802 |
| net_avg_win | 36.6092 |
| net_avg_loss | -51.0075 |
| avg_hold_time_bars | 10.5461 |
| exposure | 0.4995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
