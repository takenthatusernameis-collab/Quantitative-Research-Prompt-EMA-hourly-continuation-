# EMA Hourly Continuation — RLC/USDT P21_50

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.6881 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -2.8345 |
| sortino_ratio | -0.9458 |
| max_drawdown | 0.6730 |
| cagr | -0.3514 |
| net_avg_win | 54.9829 |
| net_avg_loss | -76.7287 |
| avg_hold_time_bars | 6.8785 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
