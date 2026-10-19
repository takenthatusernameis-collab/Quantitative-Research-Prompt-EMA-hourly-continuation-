# EMA Hourly Continuation — CFX/USDT P8_50

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.6023 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -6.0471 |
| sortino_ratio | -2.7431 |
| max_drawdown | 0.9650 |
| cagr | -0.7343 |
| net_avg_win | 30.1658 |
| net_avg_loss | -43.3664 |
| avg_hold_time_bars | 10.0825 |
| exposure | 0.4780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
