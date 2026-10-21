# EMA Hourly Continuation — TAO/USDT P34_55

**Symbol:** TAO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.7476 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -1.5149 |
| sortino_ratio | -0.3442 |
| max_drawdown | 0.3657 |
| cagr | -0.1464 |
| net_avg_win | 79.0148 |
| net_avg_loss | -100.7719 |
| avg_hold_time_bars | 6.0397 |
| exposure | 0.0692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
