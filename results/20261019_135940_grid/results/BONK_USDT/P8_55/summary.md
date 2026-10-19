# EMA Hourly Continuation — BONK/USDT P8_55

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.5974 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -5.7643 |
| sortino_ratio | -2.6404 |
| max_drawdown | 0.9648 |
| cagr | -0.7254 |
| net_avg_win | 28.8686 |
| net_avg_loss | -41.1583 |
| avg_hold_time_bars | 9.4274 |
| exposure | 0.4602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
