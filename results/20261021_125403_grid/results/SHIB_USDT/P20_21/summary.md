# EMA Hourly Continuation — SHIB/USDT P20_21

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 121 |
| net_profit_factor | 0.7560 |
| net_win_rate | 0.5289 |
| gross_profit_factor | 1.1171 |
| gross_win_rate | 0.5289 |
| sharpe_ratio | -0.9553 |
| sortino_ratio | -0.1519 |
| max_drawdown | 0.2322 |
| cagr | -0.0673 |
| net_avg_win | 77.7049 |
| net_avg_loss | -115.4145 |
| avg_hold_time_bars | 4.0000 |
| exposure | 0.0220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
