# EMA Hourly Continuation — AURORA/USDT P34_89

**Symbol:** AURORA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6484 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.8785 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -2.7828 |
| sortino_ratio | -0.7440 |
| max_drawdown | 0.6130 |
| cagr | -0.2894 |
| net_avg_win | 65.5716 |
| net_avg_loss | -86.2249 |
| avg_hold_time_bars | 15.3210 |
| exposure | 0.2451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
