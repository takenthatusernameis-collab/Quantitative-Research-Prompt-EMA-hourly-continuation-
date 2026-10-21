# EMA Hourly Continuation — MASK/USDT P50_55

**Symbol:** MASK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.5558 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.4666 |
| sortino_ratio | -0.5010 |
| max_drawdown | 0.4501 |
| cagr | -0.2093 |
| net_avg_win | 56.3083 |
| net_avg_loss | -97.3688 |
| avg_hold_time_bars | 5.4257 |
| exposure | 0.0498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
