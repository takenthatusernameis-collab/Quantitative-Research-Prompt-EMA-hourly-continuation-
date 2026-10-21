# EMA Hourly Continuation — ACE/USDT P20_21

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.5950 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9263 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -2.5220 |
| sortino_ratio | -0.5578 |
| max_drawdown | 0.4854 |
| cagr | -0.2260 |
| net_avg_win | 61.8720 |
| net_avg_loss | -92.5246 |
| avg_hold_time_bars | 6.7458 |
| exposure | 0.0733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
