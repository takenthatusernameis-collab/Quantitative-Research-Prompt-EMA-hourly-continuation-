# EMA Hourly Continuation — MEW/USDT P12_50

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.5910 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8737 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -5.7625 |
| sortino_ratio | -2.5965 |
| max_drawdown | 0.9568 |
| cagr | -0.7096 |
| net_avg_win | 29.5599 |
| net_avg_loss | -42.0837 |
| avg_hold_time_bars | 7.9804 |
| exposure | 0.3707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
