# EMA Hourly Continuation — AGLD/USDT P8_89

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.8211 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.6439 |
| sortino_ratio | -0.5533 |
| max_drawdown | 0.5582 |
| cagr | -0.2264 |
| net_avg_win | 79.2282 |
| net_avg_loss | -94.7781 |
| avg_hold_time_bars | 24.9659 |
| exposure | 0.6293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
