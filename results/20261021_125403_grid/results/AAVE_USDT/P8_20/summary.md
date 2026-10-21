# EMA Hourly Continuation — AAVE/USDT P8_20

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7029 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -2.4933 |
| sortino_ratio | -0.7448 |
| max_drawdown | 0.5992 |
| cagr | -0.2889 |
| net_avg_win | 65.1288 |
| net_avg_loss | -85.3072 |
| avg_hold_time_bars | 6.5734 |
| exposure | 0.1303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
