# EMA Hourly Continuation — BTC/USDT P8_12

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2075 |
| net_profit_factor | 0.0473 |
| net_win_rate | 0.2275 |
| gross_profit_factor | 0.5999 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -25.9247 |
| sortino_ratio | -18.2417 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 1.0514 |
| net_avg_loss | -6.5479 |
| avg_hold_time_bars | 1.8294 |
| exposure | 0.1518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
