# EMA Hourly Continuation — NYM/USDT P20_144

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.5405 |
| net_win_rate | 0.4123 |
| gross_profit_factor | 0.7257 |
| gross_win_rate | 0.4123 |
| sharpe_ratio | -3.4389 |
| sortino_ratio | -0.8524 |
| max_drawdown | 0.6333 |
| cagr | -0.3271 |
| net_avg_win | 58.3707 |
| net_avg_loss | -75.7743 |
| avg_hold_time_bars | 36.9805 |
| exposure | 0.5177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
