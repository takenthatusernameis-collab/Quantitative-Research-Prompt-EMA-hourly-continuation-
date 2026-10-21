# EMA Hourly Continuation — AURORA/USDT P89_144

**Symbol:** AURORA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.6063 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -2.4302 |
| sortino_ratio | -0.5093 |
| max_drawdown | 0.4510 |
| cagr | -0.2097 |
| net_avg_win | 68.7053 |
| net_avg_loss | -97.6919 |
| avg_hold_time_bars | 8.5741 |
| exposure | 0.0842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
