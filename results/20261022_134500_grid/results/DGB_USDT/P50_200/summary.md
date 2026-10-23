# EMA Hourly Continuation — DGB/USDT P50_200

**Symbol:** DGB/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5954 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -3.7202 |
| sortino_ratio | -1.0837 |
| max_drawdown | 0.7434 |
| cagr | -0.4104 |
| net_avg_win | 55.1653 |
| net_avg_loss | -75.3464 |
| avg_hold_time_bars | 20.4600 |
| exposure | 0.4064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
