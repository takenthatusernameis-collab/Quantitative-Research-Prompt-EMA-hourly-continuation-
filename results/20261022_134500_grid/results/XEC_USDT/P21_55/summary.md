# EMA Hourly Continuation — XEC/USDT P21_55

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1025 |
| net_profit_factor | 0.4882 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -7.8873 |
| sortino_ratio | -3.5749 |
| max_drawdown | 0.9879 |
| cagr | -0.8251 |
| net_avg_win | 20.5297 |
| net_avg_loss | -34.0993 |
| avg_hold_time_bars | 5.5659 |
| exposure | 0.2582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
