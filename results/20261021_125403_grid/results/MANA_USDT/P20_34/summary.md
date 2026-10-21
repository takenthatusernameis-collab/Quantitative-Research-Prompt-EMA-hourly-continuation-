# EMA Hourly Continuation — MANA/USDT P20_34

**Symbol:** MANA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7262 |
| net_win_rate | 0.5221 |
| gross_profit_factor | 1.0640 |
| gross_win_rate | 0.5221 |
| sharpe_ratio | -1.6701 |
| sortino_ratio | -0.4440 |
| max_drawdown | 0.4000 |
| cagr | -0.1823 |
| net_avg_win | 59.4404 |
| net_avg_loss | -89.4345 |
| avg_hold_time_bars | 5.1888 |
| exposure | 0.0800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
