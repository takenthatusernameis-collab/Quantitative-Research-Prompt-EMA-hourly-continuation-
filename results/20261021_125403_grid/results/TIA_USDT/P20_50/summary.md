# EMA Hourly Continuation — TIA/USDT P20_50

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.8774 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.1040 |
| gross_win_rate | 0.5268 |
| sharpe_ratio | -0.8804 |
| sortino_ratio | -0.2849 |
| max_drawdown | 0.3815 |
| cagr | -0.1259 |
| net_avg_win | 77.4951 |
| net_avg_loss | -98.3391 |
| avg_hold_time_bars | 7.4652 |
| exposure | 0.1707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
