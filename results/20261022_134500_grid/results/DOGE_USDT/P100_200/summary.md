# EMA Hourly Continuation — DOGE/USDT P100_200

**Symbol:** DOGE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9676 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -4.1575 |
| sortino_ratio | -1.1741 |
| max_drawdown | 0.7661 |
| cagr | -0.4353 |
| net_avg_win | 47.9089 |
| net_avg_loss | -78.1397 |
| avg_hold_time_bars | 9.3713 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
