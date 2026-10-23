# EMA Hourly Continuation — SKL/USDT P8_34

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1485 |
| net_profit_factor | 0.4977 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8709 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -8.3711 |
| sortino_ratio | -4.5276 |
| max_drawdown | 0.9962 |
| cagr | -0.8901 |
| net_avg_win | 14.5587 |
| net_avg_loss | -24.5746 |
| avg_hold_time_bars | 4.9697 |
| exposure | 0.3355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
