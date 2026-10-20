# EMA Hourly Continuation — UQC/USDT P12_21

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.0847 |
| net_win_rate | 0.2043 |
| gross_profit_factor | 0.2837 |
| gross_win_rate | 0.2487 |
| sharpe_ratio | -13.0348 |
| sortino_ratio | -4.6340 |
| max_drawdown | 0.9986 |
| cagr | -0.9255 |
| net_avg_win | 8.0331 |
| net_avg_loss | -24.3515 |
| avg_hold_time_bars | 21.4725 |
| exposure | 0.5471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
