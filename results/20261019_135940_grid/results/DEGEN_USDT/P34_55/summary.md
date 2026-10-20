# EMA Hourly Continuation — DEGEN/USDT P34_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.5214 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.8235 |
| gross_win_rate | 0.4264 |
| sharpe_ratio | -7.7529 |
| sortino_ratio | -3.1855 |
| max_drawdown | 0.9804 |
| cagr | -0.7909 |
| net_avg_win | 30.7724 |
| net_avg_loss | -40.7976 |
| avg_hold_time_bars | 3.2615 |
| exposure | 0.1261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
