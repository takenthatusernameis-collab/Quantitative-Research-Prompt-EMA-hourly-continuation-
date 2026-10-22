# EMA Hourly Continuation — HBAR/USDT P8_200

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7008 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0419 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -2.2289 |
| sortino_ratio | -0.6193 |
| max_drawdown | 0.5576 |
| cagr | -0.2604 |
| net_avg_win | 62.2226 |
| net_avg_loss | -90.5956 |
| avg_hold_time_bars | 44.1313 |
| exposure | 0.7944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
