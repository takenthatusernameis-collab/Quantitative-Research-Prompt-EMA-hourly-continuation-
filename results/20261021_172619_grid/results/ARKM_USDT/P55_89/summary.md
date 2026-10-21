# EMA Hourly Continuation — ARKM/USDT P55_89

**Symbol:** ARKM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8071 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0605 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -1.2132 |
| sortino_ratio | -0.3071 |
| max_drawdown | 0.3368 |
| cagr | -0.1321 |
| net_avg_win | 78.7518 |
| net_avg_loss | -102.7465 |
| avg_hold_time_bars | 6.5129 |
| exposure | 0.0918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
