# EMA Hourly Continuation — ANYONE/USDT P34_89

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.7365 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8683 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -1.9154 |
| sortino_ratio | -0.5579 |
| max_drawdown | 0.4609 |
| cagr | -0.2272 |
| net_avg_win | 69.6802 |
| net_avg_loss | -83.3146 |
| avg_hold_time_bars | 10.7672 |
| exposure | 0.2057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
