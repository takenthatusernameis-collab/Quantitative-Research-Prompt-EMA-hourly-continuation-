# EMA Hourly Continuation — BONK/USDT P12_55

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.6438 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9694 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -4.9785 |
| sortino_ratio | -2.2108 |
| max_drawdown | 0.9375 |
| cagr | -0.6583 |
| net_avg_win | 35.1822 |
| net_avg_loss | -49.7684 |
| avg_hold_time_bars | 8.0269 |
| exposure | 0.3667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
