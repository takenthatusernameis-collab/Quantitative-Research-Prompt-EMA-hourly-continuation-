# EMA Hourly Continuation — BICO/USDT P26_200

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6439 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8259 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -2.5085 |
| sortino_ratio | -0.6543 |
| max_drawdown | 0.5701 |
| cagr | -0.2652 |
| net_avg_win | 62.8581 |
| net_avg_loss | -80.9135 |
| avg_hold_time_bars | 38.4825 |
| exposure | 0.5982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
