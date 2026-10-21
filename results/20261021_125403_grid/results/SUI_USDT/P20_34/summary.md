# EMA Hourly Continuation — SUI/USDT P20_34

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6497 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.8726 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -2.3259 |
| sortino_ratio | -0.5763 |
| max_drawdown | 0.5146 |
| cagr | -0.2314 |
| net_avg_win | 63.6095 |
| net_avg_loss | -86.2842 |
| avg_hold_time_bars | 5.1296 |
| exposure | 0.0702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
