# EMA Hourly Continuation — IMX/USDT P20_34

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.3364 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.6765 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -9.5694 |
| sortino_ratio | -4.4811 |
| max_drawdown | 0.9966 |
| cagr | -0.8951 |
| net_avg_win | 10.7746 |
| net_avg_loss | -23.6154 |
| avg_hold_time_bars | 2.9059 |
| exposure | 0.1453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
