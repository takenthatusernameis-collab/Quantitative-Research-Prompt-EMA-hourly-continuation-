# EMA Hourly Continuation — ALEX/USDT P8_21

**Symbol:** ALEX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1425 |
| net_profit_factor | 0.4618 |
| net_win_rate | 0.3656 |
| gross_profit_factor | 0.9832 |
| gross_win_rate | 0.3930 |
| sharpe_ratio | -13.1481 |
| sortino_ratio | -6.9580 |
| max_drawdown | 0.9999 |
| cagr | -0.9744 |
| net_avg_win | 16.4697 |
| net_avg_loss | -20.5528 |
| avg_hold_time_bars | 3.9628 |
| exposure | 0.2567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
