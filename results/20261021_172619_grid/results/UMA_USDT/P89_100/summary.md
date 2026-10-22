# EMA Hourly Continuation — UMA/USDT P89_100

**Symbol:** UMA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 0.6365 |
| net_win_rate | 0.5257 |
| gross_profit_factor | 1.0761 |
| gross_win_rate | 0.5257 |
| sharpe_ratio | -1.7293 |
| sortino_ratio | -0.3300 |
| max_drawdown | 0.3303 |
| cagr | -0.1393 |
| net_avg_win | 59.7379 |
| net_avg_loss | -104.0368 |
| avg_hold_time_bars | 6.3886 |
| exposure | 0.0508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
