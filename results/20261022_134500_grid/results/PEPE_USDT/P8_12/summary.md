# EMA Hourly Continuation — PEPE/USDT P8_12

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1854 |
| net_profit_factor | 0.3536 |
| net_win_rate | 0.3830 |
| gross_profit_factor | 0.8011 |
| gross_win_rate | 0.4207 |
| sharpe_ratio | -16.9370 |
| sortino_ratio | -10.4496 |
| max_drawdown | 1.0000 |
| cagr | -0.9964 |
| net_avg_win | 7.7058 |
| net_avg_loss | -13.5237 |
| avg_hold_time_bars | 1.6472 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
