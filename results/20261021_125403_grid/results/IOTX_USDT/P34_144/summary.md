# EMA Hourly Continuation — IOTX/USDT P34_144

**Symbol:** IOTX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7613 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -1.6142 |
| sortino_ratio | -0.4598 |
| max_drawdown | 0.4753 |
| cagr | -0.1908 |
| net_avg_win | 67.1007 |
| net_avg_loss | -85.9479 |
| avg_hold_time_bars | 21.2670 |
| exposure | 0.3838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
