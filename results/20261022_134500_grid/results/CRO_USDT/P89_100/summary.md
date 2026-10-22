# EMA Hourly Continuation — CRO/USDT P89_100

**Symbol:** CRO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.1540 |
| net_win_rate | 0.3107 |
| gross_profit_factor | 0.6270 |
| gross_win_rate | 0.3981 |
| sharpe_ratio | -11.9063 |
| sortino_ratio | -4.4712 |
| max_drawdown | 0.9979 |
| cagr | -0.9144 |
| net_avg_win | 9.4634 |
| net_avg_loss | -27.6905 |
| avg_hold_time_bars | 2.1165 |
| exposure | 0.0595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
