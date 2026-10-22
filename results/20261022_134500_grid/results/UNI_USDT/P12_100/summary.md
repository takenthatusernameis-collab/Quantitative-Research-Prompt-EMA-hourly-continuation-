# EMA Hourly Continuation — UNI/USDT P12_100

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.6104 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.9131 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -4.3729 |
| sortino_ratio | -1.6105 |
| max_drawdown | 0.8628 |
| cagr | -0.5413 |
| net_avg_win | 41.6539 |
| net_avg_loss | -59.7338 |
| avg_hold_time_bars | 17.2471 |
| exposure | 0.5425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
