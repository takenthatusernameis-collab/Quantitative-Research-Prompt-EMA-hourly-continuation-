# EMA Hourly Continuation — EDU/USDT P55_100

**Symbol:** EDU/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.6775 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9015 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -2.3360 |
| sortino_ratio | -0.6699 |
| max_drawdown | 0.5609 |
| cagr | -0.2650 |
| net_avg_win | 58.4782 |
| net_avg_loss | -79.3589 |
| avg_hold_time_bars | 7.7309 |
| exposure | 0.1417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
