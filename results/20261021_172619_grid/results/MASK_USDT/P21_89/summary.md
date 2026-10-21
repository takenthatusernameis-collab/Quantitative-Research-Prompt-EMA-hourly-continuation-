# EMA Hourly Continuation — MASK/USDT P21_89

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5744 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.7946 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -3.8430 |
| sortino_ratio | -1.2494 |
| max_drawdown | 0.7799 |
| cagr | -0.4404 |
| net_avg_win | 44.2564 |
| net_avg_loss | -61.9536 |
| avg_hold_time_bars | 16.7238 |
| exposure | 0.3991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
