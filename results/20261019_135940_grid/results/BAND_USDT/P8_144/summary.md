# EMA Hourly Continuation — BAND/USDT P8_144

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.9068 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -3.3034 |
| sortino_ratio | -0.9874 |
| max_drawdown | 0.7107 |
| cagr | -0.3776 |
| net_avg_win | 63.5627 |
| net_avg_loss | -81.0445 |
| avg_hold_time_bars | 35.8802 |
| exposure | 0.7452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
