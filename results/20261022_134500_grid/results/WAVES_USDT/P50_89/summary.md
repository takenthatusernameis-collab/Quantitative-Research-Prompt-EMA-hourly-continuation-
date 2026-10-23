# EMA Hourly Continuation — WAVES/USDT P50_89

**Symbol:** WAVES/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 777 |
| net_profit_factor | 0.3493 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.7296 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -8.0273 |
| sortino_ratio | -3.1651 |
| max_drawdown | 0.9828 |
| cagr | -0.7959 |
| net_avg_win | 16.0113 |
| net_avg_loss | -33.6671 |
| avg_hold_time_bars | 4.8739 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
