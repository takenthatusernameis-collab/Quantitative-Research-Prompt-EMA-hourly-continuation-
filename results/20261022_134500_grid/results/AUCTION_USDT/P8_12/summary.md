# EMA Hourly Continuation — AUCTION/USDT P8_12

**Symbol:** AUCTION/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1610 |
| net_profit_factor | 0.3327 |
| net_win_rate | 0.3714 |
| gross_profit_factor | 0.8645 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -15.5755 |
| sortino_ratio | -8.9621 |
| max_drawdown | 1.0000 |
| cagr | -0.9909 |
| net_avg_win | 8.3385 |
| net_avg_loss | -14.8087 |
| avg_hold_time_bars | 2.9826 |
| exposure | 0.2173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
