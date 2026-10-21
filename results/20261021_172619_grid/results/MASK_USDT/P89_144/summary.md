# EMA Hourly Continuation — MASK/USDT P89_144

**Symbol:** MASK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.6794 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -2.0230 |
| sortino_ratio | -0.5114 |
| max_drawdown | 0.4932 |
| cagr | -0.2127 |
| net_avg_win | 59.0798 |
| net_avg_loss | -92.0695 |
| avg_hold_time_bars | 6.7492 |
| exposure | 0.0966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
