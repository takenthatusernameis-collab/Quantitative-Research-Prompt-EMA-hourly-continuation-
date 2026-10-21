# EMA Hourly Continuation — CATI/USDT P12_21

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.5732 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.7875 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -2.9607 |
| sortino_ratio | -0.7173 |
| max_drawdown | 0.5020 |
| cagr | -0.2814 |
| net_avg_win | 63.0257 |
| net_avg_loss | -86.9838 |
| avg_hold_time_bars | 7.9417 |
| exposure | 0.1045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
