# EMA Hourly Continuation — IOTA/USDT P89_200

**Symbol:** IOTA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -3.2738 |
| sortino_ratio | -0.8887 |
| max_drawdown | 0.6743 |
| cagr | -0.3464 |
| net_avg_win | 50.7398 |
| net_avg_loss | -77.8730 |
| avg_hold_time_bars | 11.9568 |
| exposure | 0.2011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
