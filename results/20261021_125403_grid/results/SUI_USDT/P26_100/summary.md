# EMA Hourly Continuation — SUI/USDT P26_100

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.9431 |
| net_win_rate | 0.5429 |
| gross_profit_factor | 1.1743 |
| gross_win_rate | 0.5429 |
| sharpe_ratio | -0.3261 |
| sortino_ratio | -0.0968 |
| max_drawdown | 0.2751 |
| cagr | -0.0494 |
| net_avg_win | 86.8243 |
| net_avg_loss | -109.3214 |
| avg_hold_time_bars | 16.4833 |
| exposure | 0.3147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
