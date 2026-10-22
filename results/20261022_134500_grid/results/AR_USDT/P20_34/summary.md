# EMA Hourly Continuation — AR/USDT P20_34

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1165 |
| net_profit_factor | 0.3596 |
| net_win_rate | 0.4069 |
| gross_profit_factor | 0.6745 |
| gross_win_rate | 0.4215 |
| sharpe_ratio | -10.4140 |
| sortino_ratio | -5.0299 |
| max_drawdown | 0.9983 |
| cagr | -0.9202 |
| net_avg_win | 11.8236 |
| net_avg_loss | -22.5570 |
| avg_hold_time_bars | 2.6601 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
