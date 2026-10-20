# EMA Hourly Continuation — AIOZ/USDT P20_34

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1220 |
| net_profit_factor | 0.4512 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.8176 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -10.3366 |
| sortino_ratio | -5.0787 |
| max_drawdown | 0.9985 |
| cagr | -0.9228 |
| net_avg_win | 16.2875 |
| net_avg_loss | -25.4090 |
| avg_hold_time_bars | 2.7557 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
