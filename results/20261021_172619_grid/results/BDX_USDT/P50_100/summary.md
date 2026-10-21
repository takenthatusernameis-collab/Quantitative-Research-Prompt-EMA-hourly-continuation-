# EMA Hourly Continuation — BDX/USDT P50_100

**Symbol:** BDX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.4432 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.7376 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -3.8618 |
| sortino_ratio | -0.8864 |
| max_drawdown | 0.6518 |
| cagr | -0.3360 |
| net_avg_win | 47.3506 |
| net_avg_loss | -78.4875 |
| avg_hold_time_bars | 7.9294 |
| exposure | 0.0919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
