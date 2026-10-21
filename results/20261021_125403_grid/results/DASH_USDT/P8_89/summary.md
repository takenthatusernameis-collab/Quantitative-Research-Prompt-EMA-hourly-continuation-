# EMA Hourly Continuation — DASH/USDT P8_89

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7730 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9793 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -1.8138 |
| sortino_ratio | -0.5907 |
| max_drawdown | 0.5182 |
| cagr | -0.2388 |
| net_avg_win | 66.0002 |
| net_avg_loss | -83.1044 |
| avg_hold_time_bars | 26.5067 |
| exposure | 0.6253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
