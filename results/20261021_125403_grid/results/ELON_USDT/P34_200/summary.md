# EMA Hourly Continuation — ELON/USDT P34_200

**Symbol:** ELON/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6668 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8299 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -2.2275 |
| sortino_ratio | -0.5638 |
| max_drawdown | 0.4903 |
| cagr | -0.2281 |
| net_avg_win | 65.9631 |
| net_avg_loss | -82.9169 |
| avg_hold_time_bars | 30.8585 |
| exposure | 0.4460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
