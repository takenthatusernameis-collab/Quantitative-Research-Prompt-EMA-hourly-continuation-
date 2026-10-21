# EMA Hourly Continuation — XEC/USDT P89_100

**Symbol:** XEC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.5069 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -2.8168 |
| sortino_ratio | -0.5602 |
| max_drawdown | 0.4846 |
| cagr | -0.2261 |
| net_avg_win | 56.2649 |
| net_avg_loss | -91.9618 |
| avg_hold_time_bars | 4.2604 |
| exposure | 0.0370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
