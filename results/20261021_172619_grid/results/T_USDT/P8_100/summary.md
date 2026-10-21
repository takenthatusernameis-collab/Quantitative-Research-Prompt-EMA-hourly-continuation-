# EMA Hourly Continuation — T/USDT P8_100

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7932 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0527 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -1.7761 |
| sortino_ratio | -0.5557 |
| max_drawdown | 0.5294 |
| cagr | -0.2267 |
| net_avg_win | 75.5977 |
| net_avg_loss | -96.9151 |
| avg_hold_time_bars | 29.1208 |
| exposure | 0.6325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
