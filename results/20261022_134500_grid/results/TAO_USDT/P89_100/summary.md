# EMA Hourly Continuation — TAO/USDT P89_100

**Symbol:** TAO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.2799 |
| net_win_rate | 0.3617 |
| gross_profit_factor | 0.6370 |
| gross_win_rate | 0.3865 |
| sharpe_ratio | -9.6523 |
| sortino_ratio | -3.3221 |
| max_drawdown | 0.9892 |
| cagr | -0.8355 |
| net_avg_win | 18.8475 |
| net_avg_loss | -38.1593 |
| avg_hold_time_bars | 1.7766 |
| exposure | 0.0455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
