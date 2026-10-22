# EMA Hourly Continuation — ERG/USDT P8_55

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.7081 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.8888 |
| sortino_ratio | -1.0613 |
| max_drawdown | 0.7102 |
| cagr | -0.3871 |
| net_avg_win | 54.4882 |
| net_avg_loss | -69.4534 |
| avg_hold_time_bars | 13.1913 |
| exposure | 0.3981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
