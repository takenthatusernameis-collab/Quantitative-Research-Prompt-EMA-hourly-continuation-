# EMA Hourly Continuation — QI/USDT P26_34

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7414 |
| net_win_rate | 0.5441 |
| gross_profit_factor | 1.1928 |
| gross_win_rate | 0.5441 |
| sharpe_ratio | -1.6941 |
| sortino_ratio | -0.4445 |
| max_drawdown | 0.4306 |
| cagr | -0.1823 |
| net_avg_win | 63.7803 |
| net_avg_loss | -102.6543 |
| avg_hold_time_bars | 4.3708 |
| exposure | 0.0651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
