# EMA Hourly Continuation — FLOKI/USDT P12_55

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.7368 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9058 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -2.4022 |
| sortino_ratio | -0.8381 |
| max_drawdown | 0.6355 |
| cagr | -0.3204 |
| net_avg_win | 60.7809 |
| net_avg_loss | -75.3748 |
| avg_hold_time_bars | 12.7696 |
| exposure | 0.3477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
