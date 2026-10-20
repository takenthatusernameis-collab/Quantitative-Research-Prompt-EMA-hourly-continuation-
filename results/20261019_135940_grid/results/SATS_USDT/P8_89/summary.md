# EMA Hourly Continuation — SATS/USDT P8_89

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.7140 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9767 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -2.9495 |
| sortino_ratio | -1.1100 |
| max_drawdown | 0.7419 |
| cagr | -0.4061 |
| net_avg_win | 53.5579 |
| net_avg_loss | -69.3147 |
| avg_hold_time_bars | 18.9803 |
| exposure | 0.6098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
