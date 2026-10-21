# EMA Hourly Continuation — DOT/USDT P8_100

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.8977 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1040 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -0.6686 |
| sortino_ratio | -0.2000 |
| max_drawdown | 0.3664 |
| cagr | -0.0920 |
| net_avg_win | 83.2137 |
| net_avg_loss | -103.1495 |
| avg_hold_time_bars | 35.3364 |
| exposure | 0.6923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
