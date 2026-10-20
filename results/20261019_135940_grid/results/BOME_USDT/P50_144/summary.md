# EMA Hourly Continuation — BOME/USDT P50_144

**Symbol:** BOME/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.5869 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8097 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -3.1577 |
| sortino_ratio | -0.9822 |
| max_drawdown | 0.7091 |
| cagr | -0.3691 |
| net_avg_win | 43.4771 |
| net_avg_loss | -64.0665 |
| avg_hold_time_bars | 13.5280 |
| exposure | 0.2970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
