# EMA Hourly Continuation — SYN/USDT P21_50

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6691 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8594 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -2.7747 |
| sortino_ratio | -0.9271 |
| max_drawdown | 0.6719 |
| cagr | -0.3475 |
| net_avg_win | 51.5521 |
| net_avg_loss | -68.0738 |
| avg_hold_time_bars | 7.7618 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
