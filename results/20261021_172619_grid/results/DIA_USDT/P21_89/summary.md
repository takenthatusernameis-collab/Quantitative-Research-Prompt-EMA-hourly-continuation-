# EMA Hourly Continuation — DIA/USDT P21_89

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9522 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -2.0335 |
| sortino_ratio | -0.6551 |
| max_drawdown | 0.5823 |
| cagr | -0.2606 |
| net_avg_win | 67.2760 |
| net_avg_loss | -84.2864 |
| avg_hold_time_bars | 15.7104 |
| exposure | 0.3633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
