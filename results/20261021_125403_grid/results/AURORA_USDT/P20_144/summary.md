# EMA Hourly Continuation — AURORA/USDT P20_144

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7044 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -2.1509 |
| sortino_ratio | -0.5721 |
| max_drawdown | 0.5039 |
| cagr | -0.2319 |
| net_avg_win | 69.5546 |
| net_avg_loss | -89.0804 |
| avg_hold_time_bars | 31.2686 |
| exposure | 0.4975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
