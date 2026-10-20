# EMA Hourly Continuation — IO/USDT P21_26

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.3179 |
| net_win_rate | 0.3709 |
| gross_profit_factor | 0.6589 |
| gross_win_rate | 0.3973 |
| sharpe_ratio | -12.9898 |
| sortino_ratio | -6.3788 |
| max_drawdown | 0.9996 |
| cagr | -0.9652 |
| net_avg_win | 11.4189 |
| net_avg_loss | -21.1781 |
| avg_hold_time_bars | 1.8564 |
| exposure | 0.0989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
