# EMA Hourly Continuation — XCN/USDT P100_144

**Symbol:** XCN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.3218 |
| net_win_rate | 0.3843 |
| gross_profit_factor | 0.7219 |
| gross_win_rate | 0.4070 |
| sharpe_ratio | -8.4970 |
| sortino_ratio | -3.1029 |
| max_drawdown | 0.9822 |
| cagr | -0.7950 |
| net_avg_win | 18.3327 |
| net_avg_loss | -35.5519 |
| avg_hold_time_bars | 3.9440 |
| exposure | 0.1185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
