# EMA Hourly Continuation — REQ/USDT P26_34

**Symbol:** REQ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.4020 |
| net_win_rate | 0.4094 |
| gross_profit_factor | 0.7366 |
| gross_win_rate | 0.4181 |
| sharpe_ratio | -5.4054 |
| sortino_ratio | -1.4449 |
| max_drawdown | 0.8199 |
| cagr | -0.4912 |
| net_avg_win | 39.2093 |
| net_avg_loss | -67.6057 |
| avg_hold_time_bars | 4.9035 |
| exposure | 0.0762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
