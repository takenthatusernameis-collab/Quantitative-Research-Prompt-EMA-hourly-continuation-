# EMA Hourly Continuation — METIS/USDT P89_200

**Symbol:** METIS/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.7986 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -2.5012 |
| sortino_ratio | -0.6104 |
| max_drawdown | 0.5122 |
| cagr | -0.2457 |
| net_avg_win | 68.6618 |
| net_avg_loss | -84.7565 |
| avg_hold_time_bars | 15.7407 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
