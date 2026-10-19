# EMA Hourly Continuation — PEPE/USDT P21_100

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.5684 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8339 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -4.9794 |
| sortino_ratio | -1.7031 |
| max_drawdown | 0.8778 |
| cagr | -0.5643 |
| net_avg_win | 44.1871 |
| net_avg_loss | -60.2116 |
| avg_hold_time_bars | 16.1957 |
| exposure | 0.4402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
