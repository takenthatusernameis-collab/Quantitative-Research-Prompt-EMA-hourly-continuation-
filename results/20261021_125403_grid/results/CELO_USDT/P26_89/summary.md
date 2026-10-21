# EMA Hourly Continuation — CELO/USDT P26_89

**Symbol:** CELO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.8610 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0939 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.0425 |
| sortino_ratio | -0.3306 |
| max_drawdown | 0.3539 |
| cagr | -0.1435 |
| net_avg_win | 78.8789 |
| net_avg_loss | -99.8741 |
| avg_hold_time_bars | 14.2854 |
| exposure | 0.3148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
