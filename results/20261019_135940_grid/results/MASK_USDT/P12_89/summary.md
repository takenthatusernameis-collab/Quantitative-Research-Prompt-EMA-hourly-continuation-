# EMA Hourly Continuation — MASK/USDT P12_89

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 746 |
| net_profit_factor | 0.4516 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.7448 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -6.3451 |
| sortino_ratio | -2.4217 |
| max_drawdown | 0.9522 |
| cagr | -0.6972 |
| net_avg_win | 24.4481 |
| net_avg_loss | -40.6703 |
| avg_hold_time_bars | 16.6247 |
| exposure | 0.5637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
