# EMA Hourly Continuation — LPT/USDT P21_89

**Symbol:** LPT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 795 |
| net_profit_factor | 0.5327 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.7964 |
| gross_win_rate | 0.4491 |
| sharpe_ratio | -5.6755 |
| sortino_ratio | -2.2491 |
| max_drawdown | 0.9372 |
| cagr | -0.6595 |
| net_avg_win | 30.3893 |
| net_avg_loss | -44.8713 |
| avg_hold_time_bars | 9.9245 |
| exposure | 0.3586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
