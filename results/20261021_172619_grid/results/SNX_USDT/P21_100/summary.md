# EMA Hourly Continuation — SNX/USDT P21_100

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.9566 |
| net_win_rate | 0.5445 |
| gross_profit_factor | 1.1885 |
| gross_win_rate | 0.5445 |
| sharpe_ratio | -0.2701 |
| sortino_ratio | -0.0858 |
| max_drawdown | 0.2836 |
| cagr | -0.0459 |
| net_avg_win | 93.6351 |
| net_avg_loss | -117.0201 |
| avg_hold_time_bars | 17.1056 |
| exposure | 0.3739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
