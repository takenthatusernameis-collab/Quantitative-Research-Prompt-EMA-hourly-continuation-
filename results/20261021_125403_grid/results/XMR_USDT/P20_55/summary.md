# EMA Hourly Continuation — XMR/USDT P20_55

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6377 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -3.0308 |
| sortino_ratio | -0.9211 |
| max_drawdown | 0.6589 |
| cagr | -0.3437 |
| net_avg_win | 54.4541 |
| net_avg_loss | -74.1432 |
| avg_hold_time_bars | 6.9956 |
| exposure | 0.1444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
