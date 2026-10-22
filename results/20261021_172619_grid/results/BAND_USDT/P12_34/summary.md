# EMA Hourly Continuation — BAND/USDT P12_34

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.7433 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0574 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -2.9832 |
| sortino_ratio | -1.1656 |
| max_drawdown | 0.7474 |
| cagr | -0.4124 |
| net_avg_win | 57.1851 |
| net_avg_loss | -77.9746 |
| avg_hold_time_bars | 7.1467 |
| exposure | 0.2403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
