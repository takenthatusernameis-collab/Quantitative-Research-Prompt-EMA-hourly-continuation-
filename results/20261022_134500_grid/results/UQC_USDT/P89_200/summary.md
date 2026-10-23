# EMA Hourly Continuation — UQC/USDT P89_200

**Symbol:** UQC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.2934 |
| net_win_rate | 0.2816 |
| gross_profit_factor | 0.5223 |
| gross_win_rate | 0.3102 |
| sharpe_ratio | -6.5356 |
| sortino_ratio | -1.4536 |
| max_drawdown | 0.8597 |
| cagr | -0.5410 |
| net_avg_win | 51.7387 |
| net_avg_loss | -69.1314 |
| avg_hold_time_bars | 38.8286 |
| exposure | 0.4305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
