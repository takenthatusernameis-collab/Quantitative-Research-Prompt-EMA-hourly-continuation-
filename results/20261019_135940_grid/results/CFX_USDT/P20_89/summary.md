# EMA Hourly Continuation — CFX/USDT P20_89

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6182 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -4.1365 |
| sortino_ratio | -1.4882 |
| max_drawdown | 0.8477 |
| cagr | -0.5151 |
| net_avg_win | 43.1847 |
| net_avg_loss | -63.0357 |
| avg_hold_time_bars | 13.4940 |
| exposure | 0.4060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
