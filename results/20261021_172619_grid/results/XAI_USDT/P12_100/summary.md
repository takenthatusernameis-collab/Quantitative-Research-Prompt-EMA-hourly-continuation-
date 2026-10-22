# EMA Hourly Continuation — XAI/USDT P12_100

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7908 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -1.8128 |
| sortino_ratio | -0.5466 |
| max_drawdown | 0.5556 |
| cagr | -0.2236 |
| net_avg_win | 82.7167 |
| net_avg_loss | -96.5145 |
| avg_hold_time_bars | 30.6920 |
| exposure | 0.6250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
