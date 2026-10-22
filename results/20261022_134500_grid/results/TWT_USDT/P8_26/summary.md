# EMA Hourly Continuation — TWT/USDT P8_26

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1691 |
| net_profit_factor | 0.3344 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.8117 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -13.1796 |
| sortino_ratio | -7.6889 |
| max_drawdown | 0.9999 |
| cagr | -0.9797 |
| net_avg_win | 7.1668 |
| net_avg_loss | -15.1751 |
| avg_hold_time_bars | 3.6132 |
| exposure | 0.2777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
