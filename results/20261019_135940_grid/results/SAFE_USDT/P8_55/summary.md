# EMA Hourly Continuation — SAFE/USDT P8_55

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 945 |
| net_profit_factor | 0.5704 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.8753 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -4.8392 |
| sortino_ratio | -2.0981 |
| max_drawdown | 0.9202 |
| cagr | -0.6324 |
| net_avg_win | 27.1937 |
| net_avg_loss | -42.9723 |
| avg_hold_time_bars | 11.8328 |
| exposure | 0.5121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
