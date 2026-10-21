# EMA Hourly Continuation — MINA/USDT P12_20

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.6347 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9418 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -2.7685 |
| sortino_ratio | -0.8120 |
| max_drawdown | 0.6631 |
| cagr | -0.3119 |
| net_avg_win | 51.3675 |
| net_avg_loss | -78.6374 |
| avg_hold_time_bars | 4.6459 |
| exposure | 0.0883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
