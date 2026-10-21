# EMA Hourly Continuation — ZEN/USDT P21_100

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.8154 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0090 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.3544 |
| sortino_ratio | -0.4215 |
| max_drawdown | 0.4118 |
| cagr | -0.1786 |
| net_avg_win | 72.3487 |
| net_avg_loss | -90.2492 |
| avg_hold_time_bars | 18.0890 |
| exposure | 0.3881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
