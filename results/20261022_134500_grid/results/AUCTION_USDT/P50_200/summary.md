# EMA Hourly Continuation — AUCTION/USDT P50_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5613 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8610 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -3.9552 |
| sortino_ratio | -1.1438 |
| max_drawdown | 0.7607 |
| cagr | -0.4284 |
| net_avg_win | 50.3821 |
| net_avg_loss | -72.4113 |
| avg_hold_time_bars | 21.4535 |
| exposure | 0.4175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
