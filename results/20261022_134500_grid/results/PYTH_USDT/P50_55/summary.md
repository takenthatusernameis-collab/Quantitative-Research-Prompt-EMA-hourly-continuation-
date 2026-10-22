# EMA Hourly Continuation — PYTH/USDT P50_55

**Symbol:** PYTH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 828 |
| net_profit_factor | 0.2626 |
| net_win_rate | 0.3901 |
| gross_profit_factor | 0.7681 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -10.6992 |
| sortino_ratio | -4.4295 |
| max_drawdown | 0.9975 |
| cagr | -0.9066 |
| net_avg_win | 10.9992 |
| net_avg_loss | -26.7858 |
| avg_hold_time_bars | 1.5616 |
| exposure | 0.0588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
