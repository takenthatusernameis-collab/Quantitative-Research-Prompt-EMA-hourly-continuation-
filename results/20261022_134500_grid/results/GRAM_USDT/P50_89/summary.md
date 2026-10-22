# EMA Hourly Continuation — GRAM/USDT P50_89

**Symbol:** GRAM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.4035 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.9499 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -7.7024 |
| sortino_ratio | -2.9050 |
| max_drawdown | 0.9767 |
| cagr | -0.7704 |
| net_avg_win | 21.3515 |
| net_avg_loss | -40.7709 |
| avg_hold_time_bars | 4.2225 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
