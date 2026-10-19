# EMA Hourly Continuation — BONK/USDT P8_21

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1679 |
| net_profit_factor | 0.5328 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.9294 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -11.0822 |
| sortino_ratio | -6.3595 |
| max_drawdown | 0.9997 |
| cagr | -0.9606 |
| net_avg_win | 15.7715 |
| net_avg_loss | -22.3847 |
| avg_hold_time_bars | 2.7606 |
| exposure | 0.2107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
