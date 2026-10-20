# EMA Hourly Continuation — FLUX/USDT P55_144

**Symbol:** FLUX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6063 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9695 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -3.1079 |
| sortino_ratio | -0.9837 |
| max_drawdown | 0.7045 |
| cagr | -0.3734 |
| net_avg_win | 43.6054 |
| net_avg_loss | -69.3626 |
| avg_hold_time_bars | 11.9054 |
| exposure | 0.2690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
