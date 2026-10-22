# EMA Hourly Continuation — CWEB/USDT P26_34

**Symbol:** CWEB/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.1920 |
| net_win_rate | 0.2177 |
| gross_profit_factor | 0.5783 |
| gross_win_rate | 0.2532 |
| sharpe_ratio | -18.4346 |
| sortino_ratio | -9.1626 |
| max_drawdown | 1.0000 |
| cagr | -0.9942 |
| net_avg_win | 10.7511 |
| net_avg_loss | -15.5869 |
| avg_hold_time_bars | 3.0305 |
| exposure | 0.1398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
