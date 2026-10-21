# EMA Hourly Continuation — ROSE/USDT P8_100

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.9324 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.1095 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -0.4523 |
| sortino_ratio | -0.1400 |
| max_drawdown | 0.3149 |
| cagr | -0.0683 |
| net_avg_win | 91.9230 |
| net_avg_loss | -110.3510 |
| avg_hold_time_bars | 32.2143 |
| exposure | 0.6765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
