# EMA Hourly Continuation — NMR/USDT P12_26

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.7365 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0710 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -2.6499 |
| sortino_ratio | -0.9052 |
| max_drawdown | 0.6608 |
| cagr | -0.3384 |
| net_avg_win | 63.1051 |
| net_avg_loss | -88.1470 |
| avg_hold_time_bars | 5.4113 |
| exposure | 0.1387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
