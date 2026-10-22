# EMA Hourly Continuation — RPL/USDT P8_12

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6310 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -3.7873 |
| sortino_ratio | -1.2147 |
| max_drawdown | 0.7627 |
| cagr | -0.4286 |
| net_avg_win | 54.7943 |
| net_avg_loss | -76.1877 |
| avg_hold_time_bars | 4.9921 |
| exposure | 0.1141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
