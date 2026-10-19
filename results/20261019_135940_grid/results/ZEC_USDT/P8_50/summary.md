# EMA Hourly Continuation — ZEC/USDT P8_50

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.5774 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -5.0282 |
| sortino_ratio | -2.3415 |
| max_drawdown | 0.9416 |
| cagr | -0.6760 |
| net_avg_win | 24.1240 |
| net_avg_loss | -39.3432 |
| avg_hold_time_bars | 9.0073 |
| exposure | 0.4500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
