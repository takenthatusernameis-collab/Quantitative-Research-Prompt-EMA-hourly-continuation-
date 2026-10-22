# EMA Hourly Continuation — RUNE/USDT P12_200

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.6709 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.9099 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -2.0509 |
| sortino_ratio | -0.4910 |
| max_drawdown | 0.4682 |
| cagr | -0.2059 |
| net_avg_win | 66.8714 |
| net_avg_loss | -87.2947 |
| avg_hold_time_bars | 60.8746 |
| exposure | 0.7941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
