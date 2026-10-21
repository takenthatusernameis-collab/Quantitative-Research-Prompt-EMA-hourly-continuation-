# EMA Hourly Continuation — DASH/USDT P55_89

**Symbol:** DASH/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7171 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 1.0025 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.7645 |
| sortino_ratio | -0.4247 |
| max_drawdown | 0.4091 |
| cagr | -0.1765 |
| net_avg_win | 69.8641 |
| net_avg_loss | -96.7358 |
| avg_hold_time_bars | 6.3096 |
| exposure | 0.0806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
