# EMA Hourly Continuation — FIDA/USDT P20_34

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6531 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9511 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -3.0144 |
| sortino_ratio | -0.9552 |
| max_drawdown | 0.6757 |
| cagr | -0.3556 |
| net_avg_win | 52.5460 |
| net_avg_loss | -76.6289 |
| avg_hold_time_bars | 5.5854 |
| exposure | 0.1243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
