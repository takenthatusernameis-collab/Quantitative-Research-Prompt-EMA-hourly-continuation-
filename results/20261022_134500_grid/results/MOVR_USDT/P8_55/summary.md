# EMA Hourly Continuation — MOVR/USDT P8_55

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1106 |
| net_profit_factor | 0.5303 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8638 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -6.1311 |
| sortino_ratio | -2.8619 |
| max_drawdown | 0.9691 |
| cagr | -0.7492 |
| net_avg_win | 21.7105 |
| net_avg_loss | -34.2723 |
| avg_hold_time_bars | 9.9774 |
| exposure | 0.5016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
