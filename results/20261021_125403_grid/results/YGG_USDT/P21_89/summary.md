# EMA Hourly Continuation — YGG/USDT P21_89

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.8356 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0383 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.5018 |
| sortino_ratio | -0.5023 |
| max_drawdown | 0.4974 |
| cagr | -0.2079 |
| net_avg_win | 81.8213 |
| net_avg_loss | -99.7310 |
| avg_hold_time_bars | 13.7697 |
| exposure | 0.3408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
