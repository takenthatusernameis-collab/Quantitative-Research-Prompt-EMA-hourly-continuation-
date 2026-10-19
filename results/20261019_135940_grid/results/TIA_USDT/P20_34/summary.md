# EMA Hourly Continuation — TIA/USDT P20_34

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1130 |
| net_profit_factor | 0.4900 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.9411 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -8.6704 |
| sortino_ratio | -4.0975 |
| max_drawdown | 0.9945 |
| cagr | -0.8722 |
| net_avg_win | 19.1453 |
| net_avg_loss | -30.8976 |
| avg_hold_time_bars | 2.7274 |
| exposure | 0.1401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
