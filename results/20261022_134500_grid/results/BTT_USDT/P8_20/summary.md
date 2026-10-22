# EMA Hourly Continuation — BTT/USDT P8_20

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1756 |
| net_profit_factor | 0.2091 |
| net_win_rate | 0.2916 |
| gross_profit_factor | 0.6973 |
| gross_win_rate | 0.3713 |
| sharpe_ratio | -21.8643 |
| sortino_ratio | -13.8590 |
| max_drawdown | 1.0000 |
| cagr | -0.9995 |
| net_avg_win | 5.1638 |
| net_avg_loss | -10.1639 |
| avg_hold_time_bars | 3.1162 |
| exposure | 0.2487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
