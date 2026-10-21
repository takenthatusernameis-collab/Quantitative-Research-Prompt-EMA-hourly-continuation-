# EMA Hourly Continuation — API3/USDT P8_12

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.6058 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8881 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.1442 |
| sortino_ratio | -0.7889 |
| max_drawdown | 0.6120 |
| cagr | -0.3046 |
| net_avg_win | 65.6857 |
| net_avg_loss | -90.3583 |
| avg_hold_time_bars | 6.5714 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
