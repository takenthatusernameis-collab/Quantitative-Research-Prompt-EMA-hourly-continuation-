# EMA Hourly Continuation — CATI/USDT P12_89

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6717 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8150 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.6454 |
| sortino_ratio | -0.8072 |
| max_drawdown | 0.5753 |
| cagr | -0.3120 |
| net_avg_win | 63.2461 |
| net_avg_loss | -78.4709 |
| avg_hold_time_bars | 25.4104 |
| exposure | 0.5363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
