# EMA Hourly Continuation — SOL/USDT P20_26

**Symbol:** SOL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 149 |
| net_profit_factor | 0.8161 |
| net_win_rate | 0.5503 |
| gross_profit_factor | 1.2155 |
| gross_win_rate | 0.5503 |
| sharpe_ratio | -0.7506 |
| sortino_ratio | -0.1331 |
| max_drawdown | 0.1885 |
| cagr | -0.0592 |
| net_avg_win | 76.8904 |
| net_avg_loss | -115.3101 |
| avg_hold_time_bars | 5.3960 |
| exposure | 0.0365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
