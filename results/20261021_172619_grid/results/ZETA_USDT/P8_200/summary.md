# EMA Hourly Continuation — ZETA/USDT P8_200

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8337 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9754 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -0.9098 |
| sortino_ratio | -0.2040 |
| max_drawdown | 0.3097 |
| cagr | -0.0910 |
| net_avg_win | 87.9184 |
| net_avg_loss | -102.1035 |
| avg_hold_time_bars | 73.6976 |
| exposure | 0.8271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
