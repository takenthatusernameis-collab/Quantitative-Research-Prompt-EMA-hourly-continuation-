# EMA Hourly Continuation — FET/USDT P12_26

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1480 |
| net_profit_factor | 0.4507 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8483 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -9.8848 |
| sortino_ratio | -5.3563 |
| max_drawdown | 0.9988 |
| cagr | -0.9304 |
| net_avg_win | 12.5513 |
| net_avg_loss | -21.9874 |
| avg_hold_time_bars | 2.5845 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
