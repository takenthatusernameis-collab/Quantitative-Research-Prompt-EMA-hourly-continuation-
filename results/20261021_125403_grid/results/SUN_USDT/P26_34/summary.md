# EMA Hourly Continuation — SUN/USDT P26_34

**Symbol:** SUN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.3029 |
| net_win_rate | 0.3891 |
| gross_profit_factor | 0.7436 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -6.7883 |
| sortino_ratio | -1.8224 |
| max_drawdown | 0.8961 |
| cagr | -0.5925 |
| net_avg_win | 30.4210 |
| net_avg_loss | -63.9553 |
| avg_hold_time_bars | 6.0061 |
| exposure | 0.0894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
