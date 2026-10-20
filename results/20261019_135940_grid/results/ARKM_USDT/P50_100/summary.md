# EMA Hourly Continuation — ARKM/USDT P50_100

**Symbol:** ARKM/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5246 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -4.7550 |
| sortino_ratio | -1.7124 |
| max_drawdown | 0.8799 |
| cagr | -0.5684 |
| net_avg_win | 31.1846 |
| net_avg_loss | -52.5184 |
| avg_hold_time_bars | 5.2278 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
