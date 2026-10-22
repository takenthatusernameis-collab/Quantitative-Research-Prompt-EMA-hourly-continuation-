# EMA Hourly Continuation — GLM/USDT P8_50

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.4490 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.7689 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -6.7429 |
| sortino_ratio | -3.0574 |
| max_drawdown | 0.9759 |
| cagr | -0.7708 |
| net_avg_win | 17.2370 |
| net_avg_loss | -30.6740 |
| avg_hold_time_bars | 10.2929 |
| exposure | 0.4856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
