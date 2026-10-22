# EMA Hourly Continuation — MANTA/USDT P144_200

**Symbol:** MANTA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.6854 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9214 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -1.8378 |
| sortino_ratio | -0.3947 |
| max_drawdown | 0.3829 |
| cagr | -0.1665 |
| net_avg_win | 74.0228 |
| net_avg_loss | -98.8526 |
| avg_hold_time_bars | 7.7699 |
| exposure | 0.0798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
