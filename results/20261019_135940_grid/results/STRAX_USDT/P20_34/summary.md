# EMA Hourly Continuation — STRAX/USDT P20_34

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1132 |
| net_profit_factor | 0.4179 |
| net_win_rate | 0.3984 |
| gross_profit_factor | 0.8522 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -11.1717 |
| sortino_ratio | -5.3065 |
| max_drawdown | 0.9990 |
| cagr | -0.9363 |
| net_avg_win | 15.9029 |
| net_avg_loss | -25.2010 |
| avg_hold_time_bars | 4.3260 |
| exposure | 0.2239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
