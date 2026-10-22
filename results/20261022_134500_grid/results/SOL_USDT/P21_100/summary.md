# EMA Hourly Continuation — SOL/USDT P21_100

**Symbol:** SOL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6018 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 1.0207 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -4.7298 |
| sortino_ratio | -1.7014 |
| max_drawdown | 0.8830 |
| cagr | -0.5628 |
| net_avg_win | 42.3664 |
| net_avg_loss | -63.6694 |
| avg_hold_time_bars | 12.2420 |
| exposure | 0.3656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
