# EMA Hourly Continuation — TRAC/USDT P34_200

**Symbol:** TRAC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7791 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9386 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -1.3836 |
| sortino_ratio | -0.3562 |
| max_drawdown | 0.3546 |
| cagr | -0.1517 |
| net_avg_win | 75.5618 |
| net_avg_loss | -91.2129 |
| avg_hold_time_bars | 31.4571 |
| exposure | 0.4661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
