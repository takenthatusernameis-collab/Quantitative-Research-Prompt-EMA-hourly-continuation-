# EMA Hourly Continuation — WIF/USDT P50_200

**Symbol:** WIF/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7701 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8929 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -1.3463 |
| sortino_ratio | -0.3234 |
| max_drawdown | 0.3630 |
| cagr | -0.1391 |
| net_avg_win | 77.7991 |
| net_avg_loss | -90.9247 |
| avg_hold_time_bars | 26.8737 |
| exposure | 0.3481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
