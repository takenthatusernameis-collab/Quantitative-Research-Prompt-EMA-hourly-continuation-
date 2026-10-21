# EMA Hourly Continuation — TAO/USDT P12_20

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.8769 |
| net_win_rate | 0.5343 |
| gross_profit_factor | 1.1406 |
| gross_win_rate | 0.5343 |
| sharpe_ratio | -0.5696 |
| sortino_ratio | -0.1176 |
| max_drawdown | 0.2452 |
| cagr | -0.0540 |
| net_avg_win | 85.0332 |
| net_avg_loss | -111.2626 |
| avg_hold_time_bars | 4.8676 |
| exposure | 0.0451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
