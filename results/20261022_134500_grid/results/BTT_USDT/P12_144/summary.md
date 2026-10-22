# EMA Hourly Continuation — BTT/USDT P12_144

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.4303 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.8365 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -5.9691 |
| sortino_ratio | -1.7001 |
| max_drawdown | 0.8947 |
| cagr | -0.5904 |
| net_avg_win | 39.7040 |
| net_avg_loss | -64.2892 |
| avg_hold_time_bars | 38.9396 |
| exposure | 0.7328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
