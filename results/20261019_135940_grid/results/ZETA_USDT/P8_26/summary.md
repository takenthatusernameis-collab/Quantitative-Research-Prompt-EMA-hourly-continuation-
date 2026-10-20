# EMA Hourly Continuation — ZETA/USDT P8_26

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1518 |
| net_profit_factor | 0.4602 |
| net_win_rate | 0.4262 |
| gross_profit_factor | 0.8265 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -10.1516 |
| sortino_ratio | -5.5467 |
| max_drawdown | 0.9990 |
| cagr | -0.9354 |
| net_avg_win | 13.1629 |
| net_avg_loss | -21.2473 |
| avg_hold_time_bars | 4.1094 |
| exposure | 0.2823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
