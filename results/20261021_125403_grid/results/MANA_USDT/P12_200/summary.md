# EMA Hourly Continuation — MANA/USDT P12_200

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.8080 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9573 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -0.9701 |
| sortino_ratio | -0.2083 |
| max_drawdown | 0.2644 |
| cagr | -0.0929 |
| net_avg_win | 81.6320 |
| net_avg_loss | -98.3970 |
| avg_hold_time_bars | 75.7665 |
| exposure | 0.7818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
