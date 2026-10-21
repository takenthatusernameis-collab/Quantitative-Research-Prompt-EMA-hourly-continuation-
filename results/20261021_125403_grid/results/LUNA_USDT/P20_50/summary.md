# EMA Hourly Continuation — LUNA/USDT P20_50

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.6920 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9314 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -2.7647 |
| sortino_ratio | -0.8323 |
| max_drawdown | 0.6222 |
| cagr | -0.3175 |
| net_avg_win | 66.3120 |
| net_avg_loss | -85.2214 |
| avg_hold_time_bars | 7.2185 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
