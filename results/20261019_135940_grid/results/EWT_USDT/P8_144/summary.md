# EMA Hourly Continuation — EWT/USDT P8_144

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5338 |
| net_win_rate | 0.4299 |
| gross_profit_factor | 0.7550 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -5.0474 |
| sortino_ratio | -1.8085 |
| max_drawdown | 0.9081 |
| cagr | -0.5867 |
| net_avg_win | 35.8014 |
| net_avg_loss | -50.5715 |
| avg_hold_time_bars | 20.4600 |
| exposure | 0.6166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
