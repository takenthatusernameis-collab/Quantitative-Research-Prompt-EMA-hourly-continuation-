# EMA Hourly Continuation — DASH/USDT P8_12

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1920 |
| net_profit_factor | 0.0804 |
| net_win_rate | 0.3589 |
| gross_profit_factor | 0.4847 |
| gross_win_rate | 0.4193 |
| sharpe_ratio | -19.1231 |
| sortino_ratio | -12.1560 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 1.2683 |
| net_avg_loss | -8.8333 |
| avg_hold_time_bars | 1.6297 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
