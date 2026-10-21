# EMA Hourly Continuation — TFUEL/USDT P8_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.6572 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8102 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -3.0376 |
| sortino_ratio | -0.9501 |
| max_drawdown | 0.6814 |
| cagr | -0.3547 |
| net_avg_win | 58.5537 |
| net_avg_loss | -71.7323 |
| avg_hold_time_bars | 31.2118 |
| exposure | 0.6935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
