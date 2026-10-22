# EMA Hourly Continuation — AUCTION/USDT P55_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6169 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8746 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -3.2684 |
| sortino_ratio | -0.9170 |
| max_drawdown | 0.6763 |
| cagr | -0.3534 |
| net_avg_win | 58.3697 |
| net_avg_loss | -80.9806 |
| avg_hold_time_bars | 14.6642 |
| exposure | 0.2648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
