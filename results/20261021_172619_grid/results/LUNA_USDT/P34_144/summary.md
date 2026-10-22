# EMA Hourly Continuation — LUNA/USDT P34_144

**Symbol:** LUNA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7107 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.8951 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -2.0776 |
| sortino_ratio | -0.5922 |
| max_drawdown | 0.5036 |
| cagr | -0.2385 |
| net_avg_win | 64.0642 |
| net_avg_loss | -81.5614 |
| avg_hold_time_bars | 18.5600 |
| exposure | 0.3375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
