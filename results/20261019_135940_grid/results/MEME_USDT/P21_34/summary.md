# EMA Hourly Continuation — MEME/USDT P21_34

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1171 |
| net_profit_factor | 0.3671 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.7874 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -10.1968 |
| sortino_ratio | -4.9525 |
| max_drawdown | 0.9979 |
| cagr | -0.9137 |
| net_avg_win | 11.8623 |
| net_avg_loss | -23.0857 |
| avg_hold_time_bars | 2.6003 |
| exposure | 0.1384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
