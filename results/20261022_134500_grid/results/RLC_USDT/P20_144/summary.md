# EMA Hourly Continuation — RLC/USDT P20_144

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9473 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -2.9835 |
| sortino_ratio | -1.0022 |
| max_drawdown | 0.7214 |
| cagr | -0.3764 |
| net_avg_win | 50.9423 |
| net_avg_loss | -72.2582 |
| avg_hold_time_bars | 20.1947 |
| exposure | 0.5186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
