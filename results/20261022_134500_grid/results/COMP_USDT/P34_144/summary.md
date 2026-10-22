# EMA Hourly Continuation — COMP/USDT P34_144

**Symbol:** COMP/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5437 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8916 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.8828 |
| sortino_ratio | -1.2365 |
| max_drawdown | 0.7853 |
| cagr | -0.4527 |
| net_avg_win | 38.4011 |
| net_avg_loss | -61.7058 |
| avg_hold_time_bars | 17.1272 |
| exposure | 0.4040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
