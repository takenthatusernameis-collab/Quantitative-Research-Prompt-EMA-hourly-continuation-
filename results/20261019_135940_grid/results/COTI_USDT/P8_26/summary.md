# EMA Hourly Continuation — COTI/USDT P8_26

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1618 |
| net_profit_factor | 0.5576 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.9717 |
| gross_win_rate | 0.4506 |
| sharpe_ratio | -9.8137 |
| sortino_ratio | -5.5410 |
| max_drawdown | 0.9990 |
| cagr | -0.9356 |
| net_avg_win | 17.7316 |
| net_avg_loss | -24.8670 |
| avg_hold_time_bars | 3.5630 |
| exposure | 0.2620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
