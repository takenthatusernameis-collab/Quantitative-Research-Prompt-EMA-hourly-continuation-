# EMA Hourly Continuation — BICO/USDT P8_20

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1457 |
| net_profit_factor | 0.4893 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -8.8377 |
| sortino_ratio | -4.7538 |
| max_drawdown | 0.9971 |
| cagr | -0.9018 |
| net_avg_win | 14.6749 |
| net_avg_loss | -24.2232 |
| avg_hold_time_bars | 3.7111 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
