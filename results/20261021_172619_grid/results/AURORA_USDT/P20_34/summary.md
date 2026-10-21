# EMA Hourly Continuation — AURORA/USDT P20_34

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.4433 |
| net_win_rate | 0.4157 |
| gross_profit_factor | 0.7266 |
| gross_win_rate | 0.4157 |
| sharpe_ratio | -4.9144 |
| sortino_ratio | -1.3318 |
| max_drawdown | 0.8019 |
| cagr | -0.4649 |
| net_avg_win | 42.6169 |
| net_avg_loss | -68.4021 |
| avg_hold_time_bars | 7.3174 |
| exposure | 0.1184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
