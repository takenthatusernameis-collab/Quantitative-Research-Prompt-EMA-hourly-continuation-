# EMA Hourly Continuation — SYN/USDT P20_55

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.7560 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.9443 |
| sortino_ratio | -0.6572 |
| max_drawdown | 0.5829 |
| cagr | -0.2618 |
| net_avg_win | 59.8863 |
| net_avg_loss | -77.5284 |
| avg_hold_time_bars | 8.6810 |
| exposure | 0.2202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
