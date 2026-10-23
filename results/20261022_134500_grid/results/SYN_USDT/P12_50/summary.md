# EMA Hourly Continuation — SYN/USDT P12_50

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1053 |
| net_profit_factor | 0.5602 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -5.8187 |
| sortino_ratio | -2.6391 |
| max_drawdown | 0.9607 |
| cagr | -0.7235 |
| net_avg_win | 25.3769 |
| net_avg_loss | -38.2405 |
| avg_hold_time_bars | 7.5907 |
| exposure | 0.3633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
