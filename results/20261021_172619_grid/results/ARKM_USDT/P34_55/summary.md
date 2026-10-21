# EMA Hourly Continuation — ARKM/USDT P34_55

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7557 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.6919 |
| sortino_ratio | -0.4272 |
| max_drawdown | 0.4386 |
| cagr | -0.1778 |
| net_avg_win | 78.0323 |
| net_avg_loss | -101.9324 |
| avg_hold_time_bars | 5.4323 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
