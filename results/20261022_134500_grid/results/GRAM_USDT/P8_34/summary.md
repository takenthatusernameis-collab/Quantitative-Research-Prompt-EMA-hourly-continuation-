# EMA Hourly Continuation — GRAM/USDT P8_34

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1480 |
| net_profit_factor | 0.4178 |
| net_win_rate | 0.4318 |
| gross_profit_factor | 0.8789 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -11.4369 |
| sortino_ratio | -6.1876 |
| max_drawdown | 0.9997 |
| cagr | -0.9580 |
| net_avg_win | 11.2257 |
| net_avg_loss | -20.4158 |
| avg_hold_time_bars | 4.7257 |
| exposure | 0.3179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
