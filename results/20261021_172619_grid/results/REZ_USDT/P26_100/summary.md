# EMA Hourly Continuation — REZ/USDT P26_100

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.9259 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.1072 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -0.5134 |
| sortino_ratio | -0.1604 |
| max_drawdown | 0.3500 |
| cagr | -0.0767 |
| net_avg_win | 91.7827 |
| net_avg_loss | -110.4422 |
| avg_hold_time_bars | 16.6739 |
| exposure | 0.3562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
