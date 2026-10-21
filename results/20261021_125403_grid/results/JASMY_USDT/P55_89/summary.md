# EMA Hourly Continuation — JASMY/USDT P55_89

**Symbol:** JASMY/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7505 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9908 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -1.5631 |
| sortino_ratio | -0.3836 |
| max_drawdown | 0.4107 |
| cagr | -0.1619 |
| net_avg_win | 73.7760 |
| net_avg_loss | -97.6380 |
| avg_hold_time_bars | 7.0785 |
| exposure | 0.0943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
