# EMA Hourly Continuation — BLZ/USDT P8_144

**Symbol:** BLZ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9729 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -3.1334 |
| sortino_ratio | -0.9822 |
| max_drawdown | 0.7358 |
| cagr | -0.3798 |
| net_avg_win | 59.9257 |
| net_avg_loss | -82.1378 |
| avg_hold_time_bars | 32.3831 |
| exposure | 0.7459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
