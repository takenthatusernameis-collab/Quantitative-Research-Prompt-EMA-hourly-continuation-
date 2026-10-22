# EMA Hourly Continuation — BONK/USDT P12_200

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6737 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9214 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.4166 |
| sortino_ratio | -0.6310 |
| max_drawdown | 0.6048 |
| cagr | -0.2688 |
| net_avg_win | 66.5199 |
| net_avg_loss | -89.2324 |
| avg_hold_time_bars | 47.0787 |
| exposure | 0.7618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
