# EMA Hourly Continuation — AAVE/USDT P26_144

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8867 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0686 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.6938 |
| sortino_ratio | -0.1855 |
| max_drawdown | 0.3084 |
| cagr | -0.0843 |
| net_avg_win | 86.7518 |
| net_avg_loss | -104.8678 |
| avg_hold_time_bars | 28.4104 |
| exposure | 0.4468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
