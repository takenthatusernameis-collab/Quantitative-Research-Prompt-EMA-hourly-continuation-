# EMA Hourly Continuation — EWT/USDT P144_200

**Symbol:** EWT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.4532 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8346 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -4.6551 |
| sortino_ratio | -1.2745 |
| max_drawdown | 0.8227 |
| cagr | -0.4752 |
| net_avg_win | 38.8633 |
| net_avg_loss | -69.5037 |
| avg_hold_time_bars | 4.9476 |
| exposure | 0.0859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
