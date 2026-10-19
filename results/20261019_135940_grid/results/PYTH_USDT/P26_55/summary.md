# EMA Hourly Continuation — PYTH/USDT P26_55

**Symbol:** PYTH/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.5062 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -6.2670 |
| sortino_ratio | -2.6382 |
| max_drawdown | 0.9621 |
| cagr | -0.7243 |
| net_avg_win | 23.9641 |
| net_avg_loss | -39.9505 |
| avg_hold_time_bars | 4.2996 |
| exposure | 0.1755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
