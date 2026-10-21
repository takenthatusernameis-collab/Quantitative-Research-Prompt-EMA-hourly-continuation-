# EMA Hourly Continuation — LDO/USDT P144_200

**Symbol:** LDO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.6516 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.8540 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -1.8019 |
| sortino_ratio | -0.3718 |
| max_drawdown | 0.3626 |
| cagr | -0.1569 |
| net_avg_win | 66.5171 |
| net_avg_loss | -90.1273 |
| avg_hold_time_bars | 7.3110 |
| exposure | 0.0695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
