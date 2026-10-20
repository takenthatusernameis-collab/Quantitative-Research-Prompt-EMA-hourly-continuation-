# EMA Hourly Continuation — ORDI/USDT P8_34

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1404 |
| net_profit_factor | 0.5351 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -8.4947 |
| sortino_ratio | -4.4623 |
| max_drawdown | 0.9959 |
| cagr | -0.8874 |
| net_avg_win | 18.5478 |
| net_avg_loss | -27.2533 |
| avg_hold_time_bars | 5.7101 |
| exposure | 0.3644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
