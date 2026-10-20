# EMA Hourly Continuation — AURORA/USDT P34_200

**Symbol:** AURORA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6038 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8940 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -3.1880 |
| sortino_ratio | -0.8745 |
| max_drawdown | 0.6589 |
| cagr | -0.3426 |
| net_avg_win | 56.0690 |
| net_avg_loss | -80.5729 |
| avg_hold_time_bars | 26.9790 |
| exposure | 0.4672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
