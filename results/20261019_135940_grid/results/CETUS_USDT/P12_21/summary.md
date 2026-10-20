# EMA Hourly Continuation — CETUS/USDT P12_21

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1471 |
| net_profit_factor | 0.4703 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 1.0122 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -11.5997 |
| sortino_ratio | -6.2653 |
| max_drawdown | 0.9997 |
| cagr | -0.9583 |
| net_avg_win | 14.4335 |
| net_avg_loss | -22.0482 |
| avg_hold_time_bars | 2.4133 |
| exposure | 0.1606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
