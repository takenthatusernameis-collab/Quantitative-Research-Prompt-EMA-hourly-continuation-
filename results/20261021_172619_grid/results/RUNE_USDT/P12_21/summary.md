# EMA Hourly Continuation — RUNE/USDT P12_21

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.6689 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9887 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -2.2916 |
| sortino_ratio | -0.5728 |
| max_drawdown | 0.4936 |
| cagr | -0.2305 |
| net_avg_win | 65.3788 |
| net_avg_loss | -94.5673 |
| avg_hold_time_bars | 4.5446 |
| exposure | 0.0626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
