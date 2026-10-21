# EMA Hourly Continuation — PEPE/USDT P20_26

**Symbol:** PEPE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 141 |
| net_profit_factor | 0.7743 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0185 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -0.9732 |
| sortino_ratio | -0.1659 |
| max_drawdown | 0.2459 |
| cagr | -0.0733 |
| net_avg_win | 84.0987 |
| net_avg_loss | -110.1691 |
| avg_hold_time_bars | 4.4255 |
| exposure | 0.0284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
