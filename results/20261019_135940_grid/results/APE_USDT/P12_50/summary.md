# EMA Hourly Continuation — APE/USDT P12_50

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.5864 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -6.4105 |
| sortino_ratio | -2.9642 |
| max_drawdown | 0.9737 |
| cagr | -0.7586 |
| net_avg_win | 27.6681 |
| net_avg_loss | -40.4425 |
| avg_hold_time_bars | 7.0074 |
| exposure | 0.3437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
