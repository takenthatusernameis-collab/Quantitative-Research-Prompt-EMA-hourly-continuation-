# EMA Hourly Continuation — LUNC/USDT P26_89

**Symbol:** LUNC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 779 |
| net_profit_factor | 0.4629 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.8234 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -6.7687 |
| sortino_ratio | -2.6546 |
| max_drawdown | 0.9654 |
| cagr | -0.7312 |
| net_avg_win | 24.4824 |
| net_avg_loss | -40.7507 |
| avg_hold_time_bars | 8.1977 |
| exposure | 0.2903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
