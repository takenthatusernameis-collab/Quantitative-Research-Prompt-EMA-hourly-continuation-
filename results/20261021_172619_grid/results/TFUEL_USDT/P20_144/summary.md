# EMA Hourly Continuation — TFUEL/USDT P20_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6555 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -3.4773 |
| sortino_ratio | -1.1302 |
| max_drawdown | 0.7392 |
| cagr | -0.4051 |
| net_avg_win | 59.6244 |
| net_avg_loss | -71.6052 |
| avg_hold_time_bars | 18.8885 |
| exposure | 0.4521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
