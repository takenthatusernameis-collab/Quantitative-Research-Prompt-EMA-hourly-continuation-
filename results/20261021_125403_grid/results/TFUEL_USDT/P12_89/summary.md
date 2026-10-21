# EMA Hourly Continuation — TFUEL/USDT P12_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6483 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8272 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -3.8610 |
| sortino_ratio | -1.3941 |
| max_drawdown | 0.8053 |
| cagr | -0.4732 |
| net_avg_win | 51.1279 |
| net_avg_loss | -62.9571 |
| avg_hold_time_bars | 15.6575 |
| exposure | 0.4612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
