# EMA Hourly Continuation — MEW/USDT P26_55

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.4549 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.7430 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -6.5914 |
| sortino_ratio | -2.7900 |
| max_drawdown | 0.9679 |
| cagr | -0.7437 |
| net_avg_win | 19.6861 |
| net_avg_loss | -35.5589 |
| avg_hold_time_bars | 3.8933 |
| exposure | 0.1609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
