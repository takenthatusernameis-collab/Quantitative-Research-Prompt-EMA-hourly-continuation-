# EMA Hourly Continuation — AIOZ/USDT P20_100

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.8961 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0737 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -0.6860 |
| sortino_ratio | -0.2080 |
| max_drawdown | 0.3165 |
| cagr | -0.0954 |
| net_avg_win | 83.0781 |
| net_avg_loss | -100.5505 |
| avg_hold_time_bars | 20.2635 |
| exposure | 0.4090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
