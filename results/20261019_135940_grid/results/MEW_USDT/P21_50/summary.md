# EMA Hourly Continuation — MEW/USDT P21_50

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 957 |
| net_profit_factor | 0.4775 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.7672 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -6.5693 |
| sortino_ratio | -2.8507 |
| max_drawdown | 0.9698 |
| cagr | -0.7508 |
| net_avg_win | 20.4160 |
| net_avg_loss | -35.4790 |
| avg_hold_time_bars | 4.4713 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
