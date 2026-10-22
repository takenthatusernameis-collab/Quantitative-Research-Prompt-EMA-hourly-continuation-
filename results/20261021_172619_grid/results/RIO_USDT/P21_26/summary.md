# EMA Hourly Continuation — RIO/USDT P21_26

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 166 |
| net_profit_factor | 0.5904 |
| net_win_rate | 0.4096 |
| gross_profit_factor | 0.7110 |
| gross_win_rate | 0.4096 |
| sharpe_ratio | -2.2194 |
| sortino_ratio | -0.4050 |
| max_drawdown | 0.3778 |
| cagr | -0.1706 |
| net_avg_win | 78.8555 |
| net_avg_loss | -92.6712 |
| avg_hold_time_bars | 6.0843 |
| exposure | 0.0464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
