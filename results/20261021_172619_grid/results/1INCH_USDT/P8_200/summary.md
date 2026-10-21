# EMA Hourly Continuation — 1INCH/USDT P8_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.7338 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -1.4171 |
| sortino_ratio | -0.2870 |
| max_drawdown | 0.2938 |
| cagr | -0.1248 |
| net_avg_win | 81.6853 |
| net_avg_loss | -98.9469 |
| avg_hold_time_bars | 91.9608 |
| exposure | 0.8527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
