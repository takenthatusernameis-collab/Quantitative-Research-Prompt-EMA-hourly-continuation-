# EMA Hourly Continuation — ANKR/USDT P8_55

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.5861 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.9677 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -6.1742 |
| sortino_ratio | -2.6953 |
| max_drawdown | 0.9622 |
| cagr | -0.7237 |
| net_avg_win | 31.4143 |
| net_avg_loss | -44.8011 |
| avg_hold_time_bars | 12.3365 |
| exposure | 0.5333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
