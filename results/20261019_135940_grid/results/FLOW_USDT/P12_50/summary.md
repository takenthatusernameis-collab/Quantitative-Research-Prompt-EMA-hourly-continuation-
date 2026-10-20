# EMA Hourly Continuation — FLOW/USDT P12_50

**Symbol:** FLOW/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.5317 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -6.2295 |
| sortino_ratio | -2.8162 |
| max_drawdown | 0.9688 |
| cagr | -0.7429 |
| net_avg_win | 22.7776 |
| net_avg_loss | -37.6800 |
| avg_hold_time_bars | 8.2272 |
| exposure | 0.3852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
