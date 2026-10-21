# EMA Hourly Continuation — TRAC/USDT P89_100

**Symbol:** TRAC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 152 |
| net_profit_factor | 0.7812 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0711 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -0.8962 |
| sortino_ratio | -0.1592 |
| max_drawdown | 0.1834 |
| cagr | -0.0701 |
| net_avg_win | 75.4015 |
| net_avg_loss | -104.4488 |
| avg_hold_time_bars | 5.6711 |
| exposure | 0.0392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
