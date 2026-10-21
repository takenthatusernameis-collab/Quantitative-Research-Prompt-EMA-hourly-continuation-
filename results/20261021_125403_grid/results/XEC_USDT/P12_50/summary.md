# EMA Hourly Continuation — XEC/USDT P12_50

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.6909 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9636 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -3.6721 |
| sortino_ratio | -1.4564 |
| max_drawdown | 0.8324 |
| cagr | -0.4870 |
| net_avg_win | 49.0564 |
| net_avg_loss | -65.6931 |
| avg_hold_time_bars | 9.8018 |
| exposure | 0.3424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
