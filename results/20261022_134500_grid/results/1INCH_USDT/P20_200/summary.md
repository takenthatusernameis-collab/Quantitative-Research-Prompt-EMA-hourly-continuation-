# EMA Hourly Continuation — 1INCH/USDT P20_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.6994 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 1.0269 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -1.8217 |
| sortino_ratio | -0.4280 |
| max_drawdown | 0.4190 |
| cagr | -0.1803 |
| net_avg_win | 67.2607 |
| net_avg_loss | -95.4654 |
| avg_hold_time_bars | 59.1465 |
| exposure | 0.7340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
