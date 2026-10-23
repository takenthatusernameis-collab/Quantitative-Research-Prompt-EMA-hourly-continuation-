# EMA Hourly Continuation — TFUEL/USDT P8_20

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1775 |
| net_profit_factor | 0.3498 |
| net_win_rate | 0.3786 |
| gross_profit_factor | 0.7540 |
| gross_win_rate | 0.4068 |
| sharpe_ratio | -15.5314 |
| sortino_ratio | -9.3188 |
| max_drawdown | 1.0000 |
| cagr | -0.9915 |
| net_avg_win | 8.0069 |
| net_avg_loss | -13.9443 |
| avg_hold_time_bars | 3.1031 |
| exposure | 0.2492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
