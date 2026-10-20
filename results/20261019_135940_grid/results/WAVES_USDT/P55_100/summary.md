# EMA Hourly Continuation — WAVES/USDT P55_100

**Symbol:** WAVES/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.4225 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8539 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -6.9470 |
| sortino_ratio | -2.6020 |
| max_drawdown | 0.9641 |
| cagr | -0.7294 |
| net_avg_win | 22.6409 |
| net_avg_loss | -42.0857 |
| avg_hold_time_bars | 5.4781 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
