# EMA Hourly Continuation — MEME/USDT P34_144

**Symbol:** MEME/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7099 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9831 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -2.3665 |
| sortino_ratio | -0.7213 |
| max_drawdown | 0.5953 |
| cagr | -0.2875 |
| net_avg_win | 61.5067 |
| net_avg_loss | -84.4249 |
| avg_hold_time_bars | 20.5173 |
| exposure | 0.4309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
