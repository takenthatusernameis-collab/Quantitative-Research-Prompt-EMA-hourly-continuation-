# EMA Hourly Continuation — IO/USDT P89_100

**Symbol:** IO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.3191 |
| net_win_rate | 0.4019 |
| gross_profit_factor | 0.6299 |
| gross_win_rate | 0.4100 |
| sharpe_ratio | -8.5669 |
| sortino_ratio | -3.1427 |
| max_drawdown | 0.9769 |
| cagr | -0.7965 |
| net_avg_win | 18.4566 |
| net_avg_loss | -38.8698 |
| avg_hold_time_bars | 2.1070 |
| exposure | 0.0629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
