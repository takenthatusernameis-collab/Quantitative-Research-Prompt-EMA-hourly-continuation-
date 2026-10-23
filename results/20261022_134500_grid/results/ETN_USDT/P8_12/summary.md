# EMA Hourly Continuation — ETN/USDT P8_12

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1576 |
| net_profit_factor | 0.1749 |
| net_win_rate | 0.2265 |
| gross_profit_factor | 0.3376 |
| gross_win_rate | 0.2722 |
| sharpe_ratio | -23.8189 |
| sortino_ratio | -15.2439 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 5.9385 |
| net_avg_loss | -9.9426 |
| avg_hold_time_bars | 2.1180 |
| exposure | 0.1813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
