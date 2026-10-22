# EMA Hourly Continuation — CGPT/USDT P26_89

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8370 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0414 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -1.2981 |
| sortino_ratio | -0.3972 |
| max_drawdown | 0.4237 |
| cagr | -0.1689 |
| net_avg_win | 82.6043 |
| net_avg_loss | -101.7739 |
| avg_hold_time_bars | 13.6330 |
| exposure | 0.2820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
