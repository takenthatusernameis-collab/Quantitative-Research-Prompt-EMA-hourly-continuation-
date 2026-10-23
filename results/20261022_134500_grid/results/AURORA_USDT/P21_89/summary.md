# EMA Hourly Continuation — AURORA/USDT P21_89

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.5469 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -4.8724 |
| sortino_ratio | -1.6221 |
| max_drawdown | 0.8668 |
| cagr | -0.5488 |
| net_avg_win | 41.0754 |
| net_avg_loss | -61.3437 |
| avg_hold_time_bars | 14.7717 |
| exposure | 0.3794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
