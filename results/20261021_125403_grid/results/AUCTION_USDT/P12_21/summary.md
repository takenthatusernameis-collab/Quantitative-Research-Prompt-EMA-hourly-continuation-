# EMA Hourly Continuation — AUCTION/USDT P12_21

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.4616 |
| net_win_rate | 0.4022 |
| gross_profit_factor | 0.7108 |
| gross_win_rate | 0.4059 |
| sharpe_ratio | -6.2466 |
| sortino_ratio | -2.0764 |
| max_drawdown | 0.9184 |
| cagr | -0.6251 |
| net_avg_win | 36.0186 |
| net_avg_loss | -52.5002 |
| avg_hold_time_bars | 5.3284 |
| exposure | 0.1307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
