# EMA Hourly Continuation — ERG/USDT P8_100

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.4964 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.7585 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -6.0230 |
| sortino_ratio | -2.3948 |
| max_drawdown | 0.9490 |
| cagr | -0.6922 |
| net_avg_win | 26.6976 |
| net_avg_loss | -40.9251 |
| avg_hold_time_bars | 16.2481 |
| exposure | 0.5982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
