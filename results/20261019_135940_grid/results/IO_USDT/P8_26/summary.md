# EMA Hourly Continuation — IO/USDT P8_26

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1487 |
| net_profit_factor | 0.5629 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8757 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -8.3976 |
| sortino_ratio | -4.6909 |
| max_drawdown | 0.9955 |
| cagr | -0.8985 |
| net_avg_win | 19.0204 |
| net_avg_loss | -28.0127 |
| avg_hold_time_bars | 3.7149 |
| exposure | 0.2674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
