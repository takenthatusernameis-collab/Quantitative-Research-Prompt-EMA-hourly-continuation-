# EMA Hourly Continuation — STRAX/USDT P26_34

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.4829 |
| net_win_rate | 0.4363 |
| gross_profit_factor | 0.7680 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -4.6519 |
| sortino_ratio | -1.3722 |
| max_drawdown | 0.7937 |
| cagr | -0.4686 |
| net_avg_win | 40.0738 |
| net_avg_loss | -64.2298 |
| avg_hold_time_bars | 6.3561 |
| exposure | 0.1232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
