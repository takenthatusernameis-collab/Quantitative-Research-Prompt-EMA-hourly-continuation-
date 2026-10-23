# EMA Hourly Continuation — DODO/USDT P89_200

**Symbol:** DODO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5323 |
| net_win_rate | 0.4283 |
| gross_profit_factor | 0.7904 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -4.5287 |
| sortino_ratio | -1.4134 |
| max_drawdown | 0.8162 |
| cagr | -0.4837 |
| net_avg_win | 44.1745 |
| net_avg_loss | -62.1699 |
| avg_hold_time_bars | 9.2992 |
| exposure | 0.2053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
