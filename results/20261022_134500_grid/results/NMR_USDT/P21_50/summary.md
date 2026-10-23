# EMA Hourly Continuation — NMR/USDT P21_50

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.5453 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.9488 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -7.9640 |
| sortino_ratio | -3.6371 |
| max_drawdown | 0.9892 |
| cagr | -0.8325 |
| net_avg_win | 25.6137 |
| net_avg_loss | -37.0472 |
| avg_hold_time_bars | 4.6800 |
| exposure | 0.2234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
