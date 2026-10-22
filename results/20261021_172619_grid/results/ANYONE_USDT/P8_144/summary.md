# EMA Hourly Continuation — ANYONE/USDT P8_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.9273 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0461 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -0.4202 |
| sortino_ratio | -0.1187 |
| max_drawdown | 0.2062 |
| cagr | -0.0586 |
| net_avg_win | 90.3802 |
| net_avg_loss | -103.1990 |
| avg_hold_time_bars | 40.7143 |
| exposure | 0.7201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
