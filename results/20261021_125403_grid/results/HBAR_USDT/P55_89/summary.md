# EMA Hourly Continuation — HBAR/USDT P55_89

**Symbol:** HBAR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6742 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9523 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.9062 |
| sortino_ratio | -0.4445 |
| max_drawdown | 0.4149 |
| cagr | -0.1831 |
| net_avg_win | 63.3900 |
| net_avg_loss | -91.2171 |
| avg_hold_time_bars | 6.5303 |
| exposure | 0.0784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
