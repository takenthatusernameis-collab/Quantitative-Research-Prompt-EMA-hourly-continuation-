# EMA Hourly Continuation — SOL/USDT P26_89

**Symbol:** SOL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.8121 |
| net_win_rate | 0.5207 |
| gross_profit_factor | 1.0801 |
| gross_win_rate | 0.5207 |
| sharpe_ratio | -1.3228 |
| sortino_ratio | -0.3860 |
| max_drawdown | 0.4088 |
| cagr | -0.1635 |
| net_avg_win | 72.9886 |
| net_avg_loss | -97.6287 |
| avg_hold_time_bars | 13.0243 |
| exposure | 0.2433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
