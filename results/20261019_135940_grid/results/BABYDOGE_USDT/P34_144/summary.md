# EMA Hourly Continuation — BABYDOGE/USDT P34_144

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 46 |
| net_profit_factor | 0.9274 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9895 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.1386 |
| sortino_ratio | -0.0134 |
| max_drawdown | 0.0456 |
| cagr | -0.0068 |
| net_avg_win | 95.1782 |
| net_avg_loss | -102.6262 |
| avg_hold_time_bars | 47.1739 |
| exposure | 0.0982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
