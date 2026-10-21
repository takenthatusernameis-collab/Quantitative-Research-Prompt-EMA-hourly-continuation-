# EMA Hourly Continuation — PYTH/USDT P12_20

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.7882 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0557 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.2430 |
| sortino_ratio | -0.2970 |
| max_drawdown | 0.3414 |
| cagr | -0.1279 |
| net_avg_win | 76.2231 |
| net_avg_loss | -102.4819 |
| avg_hold_time_bars | 4.4746 |
| exposure | 0.0561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
