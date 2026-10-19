# EMA Hourly Continuation — KMNO/USDT P8_89

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.7105 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -2.9071 |
| sortino_ratio | -1.0071 |
| max_drawdown | 0.6952 |
| cagr | -0.3815 |
| net_avg_win | 59.0318 |
| net_avg_loss | -77.7087 |
| avg_hold_time_bars | 23.0000 |
| exposure | 0.6350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
