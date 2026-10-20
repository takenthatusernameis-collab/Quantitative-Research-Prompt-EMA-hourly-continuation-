# EMA Hourly Continuation — SLP/USDT P8_144

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.6159 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -4.1529 |
| sortino_ratio | -1.4117 |
| max_drawdown | 0.8239 |
| cagr | -0.4908 |
| net_avg_win | 49.2059 |
| net_avg_loss | -66.4158 |
| avg_hold_time_bars | 27.7594 |
| exposure | 0.7394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
