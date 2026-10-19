# EMA Hourly Continuation — INJ/USDT P8_50

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1095 |
| net_profit_factor | 0.5901 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8887 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -5.8048 |
| sortino_ratio | -2.7030 |
| max_drawdown | 0.9642 |
| cagr | -0.7263 |
| net_avg_win | 27.2408 |
| net_avg_loss | -39.9525 |
| avg_hold_time_bars | 9.2502 |
| exposure | 0.4604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
