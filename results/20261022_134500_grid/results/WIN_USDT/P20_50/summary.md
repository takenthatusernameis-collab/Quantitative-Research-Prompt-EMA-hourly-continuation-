# EMA Hourly Continuation — WIN/USDT P20_50

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 943 |
| net_profit_factor | 0.3405 |
| net_win_rate | 0.4019 |
| gross_profit_factor | 0.8077 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -10.1401 |
| sortino_ratio | -4.4331 |
| max_drawdown | 0.9968 |
| cagr | -0.8975 |
| net_avg_win | 13.5764 |
| net_avg_loss | -26.7955 |
| avg_hold_time_bars | 4.8271 |
| exposure | 0.2069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
