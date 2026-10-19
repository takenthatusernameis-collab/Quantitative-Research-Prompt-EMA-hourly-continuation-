# EMA Hourly Continuation — THETA/USDT P144_200

**Symbol:** THETA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.4390 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.7640 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -4.7515 |
| sortino_ratio | -1.3572 |
| max_drawdown | 0.8014 |
| cagr | -0.4747 |
| net_avg_win | 36.2529 |
| net_avg_loss | -62.1137 |
| avg_hold_time_bars | 4.0819 |
| exposure | 0.0748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
