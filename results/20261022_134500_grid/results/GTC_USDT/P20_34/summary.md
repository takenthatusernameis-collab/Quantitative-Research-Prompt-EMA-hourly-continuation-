# EMA Hourly Continuation — GTC/USDT P20_34

**Symbol:** GTC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.3957 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -9.4213 |
| sortino_ratio | -4.4139 |
| max_drawdown | 0.9956 |
| cagr | -0.8833 |
| net_avg_win | 14.2001 |
| net_avg_loss | -26.4405 |
| avg_hold_time_bars | 3.2893 |
| exposure | 0.1618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
