# EMA Hourly Continuation — CFX/USDT P55_100

**Symbol:** CFX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.5056 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8353 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -5.1649 |
| sortino_ratio | -1.8033 |
| max_drawdown | 0.8890 |
| cagr | -0.5790 |
| net_avg_win | 32.8330 |
| net_avg_loss | -53.6618 |
| avg_hold_time_bars | 5.5115 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
