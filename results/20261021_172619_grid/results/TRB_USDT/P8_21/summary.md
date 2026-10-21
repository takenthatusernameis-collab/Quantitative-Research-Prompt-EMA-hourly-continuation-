# EMA Hourly Continuation — TRB/USDT P8_21

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6648 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -3.4950 |
| sortino_ratio | -1.1728 |
| max_drawdown | 0.7577 |
| cagr | -0.4166 |
| net_avg_win | 57.3656 |
| net_avg_loss | -74.4134 |
| avg_hold_time_bars | 6.1568 |
| exposure | 0.1546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
