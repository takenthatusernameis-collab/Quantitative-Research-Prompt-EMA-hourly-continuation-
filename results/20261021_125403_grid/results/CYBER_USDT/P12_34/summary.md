# EMA Hourly Continuation — CYBER/USDT P12_34

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.7675 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0602 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -2.3387 |
| sortino_ratio | -0.8744 |
| max_drawdown | 0.6489 |
| cagr | -0.3305 |
| net_avg_win | 60.4043 |
| net_avg_loss | -82.7564 |
| avg_hold_time_bars | 7.3855 |
| exposure | 0.2273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
