# EMA Hourly Continuation — CFX/USDT P20_26

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1276 |
| net_profit_factor | 0.2087 |
| net_win_rate | 0.3331 |
| gross_profit_factor | 0.6720 |
| gross_win_rate | 0.3730 |
| sharpe_ratio | -16.0695 |
| sortino_ratio | -8.4290 |
| max_drawdown | 1.0000 |
| cagr | -0.9890 |
| net_avg_win | 6.2058 |
| net_avg_loss | -14.8500 |
| avg_hold_time_bars | 1.8699 |
| exposure | 0.1085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
