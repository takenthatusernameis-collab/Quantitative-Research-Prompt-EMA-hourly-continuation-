# EMA Hourly Continuation — ETC/USDT P20_89

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.6534 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9174 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -2.8357 |
| sortino_ratio | -0.9129 |
| max_drawdown | 0.6613 |
| cagr | -0.3417 |
| net_avg_win | 50.0089 |
| net_avg_loss | -71.5750 |
| avg_hold_time_bars | 14.7732 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
