# EMA Hourly Continuation — FLOKI/USDT P8_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.8267 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9922 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -1.3484 |
| sortino_ratio | -0.4285 |
| max_drawdown | 0.4389 |
| cagr | -0.1806 |
| net_avg_win | 76.3032 |
| net_avg_loss | -91.9300 |
| avg_hold_time_bars | 29.0000 |
| exposure | 0.6499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
