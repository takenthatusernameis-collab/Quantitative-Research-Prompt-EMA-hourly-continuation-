# EMA Hourly Continuation — NEAR/USDT P8_100

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.7020 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.7828 |
| sortino_ratio | -1.0068 |
| max_drawdown | 0.7124 |
| cagr | -0.3747 |
| net_avg_win | 51.1277 |
| net_avg_loss | -70.1957 |
| avg_hold_time_bars | 22.7800 |
| exposure | 0.6730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
