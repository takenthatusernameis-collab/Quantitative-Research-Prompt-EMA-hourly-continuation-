# EMA Hourly Continuation — GALA/USDT P34_200

**Symbol:** GALA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.8414 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9900 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8627 |
| sortino_ratio | -0.2073 |
| max_drawdown | 0.2741 |
| cagr | -0.0929 |
| net_avg_win | 81.7618 |
| net_avg_loss | -97.1725 |
| avg_hold_time_bars | 40.5426 |
| exposure | 0.5197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
