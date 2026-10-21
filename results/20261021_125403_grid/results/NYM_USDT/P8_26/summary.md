# EMA Hourly Continuation — NYM/USDT P8_26

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.4572 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8404 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -4.7670 |
| sortino_ratio | -1.6299 |
| max_drawdown | 0.8576 |
| cagr | -0.5315 |
| net_avg_win | 26.9520 |
| net_avg_loss | -51.2408 |
| avg_hold_time_bars | 11.7465 |
| exposure | 0.3054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
