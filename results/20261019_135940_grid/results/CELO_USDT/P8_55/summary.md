# EMA Hourly Continuation — CELO/USDT P8_55

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1004 |
| net_profit_factor | 0.6265 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9675 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -4.9232 |
| sortino_ratio | -2.1913 |
| max_drawdown | 0.9287 |
| cagr | -0.6475 |
| net_avg_win | 32.7744 |
| net_avg_loss | -46.9705 |
| avg_hold_time_bars | 11.2131 |
| exposure | 0.5094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
