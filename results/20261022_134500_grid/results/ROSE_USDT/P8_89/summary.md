# EMA Hourly Continuation — ROSE/USDT P8_89

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.7274 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 1.0536 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -3.1819 |
| sortino_ratio | -1.2258 |
| max_drawdown | 0.7823 |
| cagr | -0.4433 |
| net_avg_win | 55.2582 |
| net_avg_loss | -75.3584 |
| avg_hold_time_bars | 18.8822 |
| exposure | 0.6411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
