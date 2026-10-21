# EMA Hourly Continuation — BNB/USDT P20_144

**Symbol:** BNB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6766 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0452 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -2.2829 |
| sortino_ratio | -0.6449 |
| max_drawdown | 0.5354 |
| cagr | -0.2533 |
| net_avg_win | 54.9299 |
| net_avg_loss | -85.9562 |
| avg_hold_time_bars | 29.6182 |
| exposure | 0.5183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
