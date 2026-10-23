# EMA Hourly Continuation — VELO/USDT P12_20

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1538 |
| net_profit_factor | 0.4656 |
| net_win_rate | 0.4285 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -11.5875 |
| sortino_ratio | -6.4248 |
| max_drawdown | 0.9997 |
| cagr | -0.9610 |
| net_avg_win | 13.2196 |
| net_avg_loss | -21.2842 |
| avg_hold_time_bars | 2.1899 |
| exposure | 0.1531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
