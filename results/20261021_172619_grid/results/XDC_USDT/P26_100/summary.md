# EMA Hourly Continuation — XDC/USDT P26_100

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7077 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0261 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -2.1299 |
| sortino_ratio | -0.6548 |
| max_drawdown | 0.5394 |
| cagr | -0.2579 |
| net_avg_win | 54.7865 |
| net_avg_loss | -80.1675 |
| avg_hold_time_bars | 14.1900 |
| exposure | 0.2954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
