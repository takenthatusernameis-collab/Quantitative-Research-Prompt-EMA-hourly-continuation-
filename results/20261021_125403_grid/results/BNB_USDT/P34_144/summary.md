# EMA Hourly Continuation — BNB/USDT P34_144

**Symbol:** BNB/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6785 |
| net_win_rate | 0.5215 |
| gross_profit_factor | 1.0712 |
| gross_win_rate | 0.5215 |
| sharpe_ratio | -2.2664 |
| sortino_ratio | -0.6500 |
| max_drawdown | 0.5398 |
| cagr | -0.2548 |
| net_avg_win | 53.5060 |
| net_avg_loss | -85.9512 |
| avg_hold_time_bars | 18.8759 |
| exposure | 0.3389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
