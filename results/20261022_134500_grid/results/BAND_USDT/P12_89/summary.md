# EMA Hourly Continuation — BAND/USDT P12_89

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.6843 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 1.0249 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -3.5560 |
| sortino_ratio | -1.2632 |
| max_drawdown | 0.7854 |
| cagr | -0.4524 |
| net_avg_win | 55.6955 |
| net_avg_loss | -73.4185 |
| avg_hold_time_bars | 18.5725 |
| exposure | 0.5387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
