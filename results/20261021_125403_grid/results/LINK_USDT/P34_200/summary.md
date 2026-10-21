# EMA Hourly Continuation — LINK/USDT P34_200

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8501 |
| net_win_rate | 0.5158 |
| gross_profit_factor | 1.0575 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -0.8064 |
| sortino_ratio | -0.1957 |
| max_drawdown | 0.2895 |
| cagr | -0.0871 |
| net_avg_win | 78.9224 |
| net_avg_loss | -98.8953 |
| avg_hold_time_bars | 35.4561 |
| exposure | 0.4593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
