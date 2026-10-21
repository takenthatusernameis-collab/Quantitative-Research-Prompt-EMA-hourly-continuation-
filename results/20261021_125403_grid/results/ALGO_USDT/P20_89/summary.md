# EMA Hourly Continuation — ALGO/USDT P20_89

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7893 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 0.9990 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -1.5950 |
| sortino_ratio | -0.5017 |
| max_drawdown | 0.4742 |
| cagr | -0.2068 |
| net_avg_win | 68.2793 |
| net_avg_loss | -87.2264 |
| avg_hold_time_bars | 15.7697 |
| exposure | 0.3455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
