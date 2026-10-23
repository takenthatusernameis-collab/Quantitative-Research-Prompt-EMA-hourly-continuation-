# EMA Hourly Continuation — HNT/USDT P8_200

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6014 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8475 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -3.0550 |
| sortino_ratio | -0.8647 |
| max_drawdown | 0.6746 |
| cagr | -0.3411 |
| net_avg_win | 52.3981 |
| net_avg_loss | -73.7169 |
| avg_hold_time_bars | 42.4020 |
| exposure | 0.7864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
