# EMA Hourly Continuation — HBAR/USDT P21_144

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.6603 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 1.0165 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -2.7426 |
| sortino_ratio | -0.8301 |
| max_drawdown | 0.6559 |
| cagr | -0.3279 |
| net_avg_win | 53.8229 |
| net_avg_loss | -79.0849 |
| avg_hold_time_bars | 27.5767 |
| exposure | 0.5804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
