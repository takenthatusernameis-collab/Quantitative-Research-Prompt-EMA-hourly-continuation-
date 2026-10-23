# EMA Hourly Continuation — PROM/USDT P8_200

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.4783 |
| net_win_rate | 0.4057 |
| gross_profit_factor | 0.7322 |
| gross_win_rate | 0.4253 |
| sharpe_ratio | -5.4153 |
| sortino_ratio | -1.7951 |
| max_drawdown | 0.8894 |
| cagr | -0.5787 |
| net_avg_win | 35.6237 |
| net_avg_loss | -50.8417 |
| avg_hold_time_bars | 28.1210 |
| exposure | 0.7184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
