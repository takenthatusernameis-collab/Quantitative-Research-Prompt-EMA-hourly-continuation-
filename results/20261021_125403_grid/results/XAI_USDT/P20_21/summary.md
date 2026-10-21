# EMA Hourly Continuation — XAI/USDT P20_21

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.5316 |
| net_win_rate | 0.4216 |
| gross_profit_factor | 0.7210 |
| gross_win_rate | 0.4216 |
| sharpe_ratio | -2.6559 |
| sortino_ratio | -0.5136 |
| max_drawdown | 0.4485 |
| cagr | -0.2110 |
| net_avg_win | 65.2504 |
| net_avg_loss | -89.4783 |
| avg_hold_time_bars | 4.3622 |
| exposure | 0.0367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
