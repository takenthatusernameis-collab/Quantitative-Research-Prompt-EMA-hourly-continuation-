# EMA Hourly Continuation — KCS/USDT P20_55

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.1959 |
| net_win_rate | 0.3281 |
| gross_profit_factor | 0.6425 |
| gross_win_rate | 0.3948 |
| sharpe_ratio | -13.8177 |
| sortino_ratio | -6.2760 |
| max_drawdown | 0.9998 |
| cagr | -0.9650 |
| net_avg_win | 7.7313 |
| net_avg_loss | -19.2762 |
| avg_hold_time_bars | 5.8719 |
| exposure | 0.2562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
