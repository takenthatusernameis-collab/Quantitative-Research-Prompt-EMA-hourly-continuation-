# EMA Hourly Continuation — PYTH/USDT P8_50

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1134 |
| net_profit_factor | 0.6692 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 1.0202 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -5.2775 |
| sortino_ratio | -2.4972 |
| max_drawdown | 0.9519 |
| cagr | -0.6985 |
| net_avg_win | 35.6853 |
| net_avg_loss | -48.3060 |
| avg_hold_time_bars | 8.5282 |
| exposure | 0.4396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
