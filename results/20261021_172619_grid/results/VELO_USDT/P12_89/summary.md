# EMA Hourly Continuation — VELO/USDT P12_89

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.8770 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0271 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -0.8754 |
| sortino_ratio | -0.2996 |
| max_drawdown | 0.3831 |
| cagr | -0.1336 |
| net_avg_win | 74.0862 |
| net_avg_loss | -88.4285 |
| avg_hold_time_bars | 17.5624 |
| exposure | 0.4542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
