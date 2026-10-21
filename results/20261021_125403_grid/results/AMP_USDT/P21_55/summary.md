# EMA Hourly Continuation — AMP/USDT P21_55

**Symbol:** AMP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.4553 |
| net_win_rate | 0.3866 |
| gross_profit_factor | 0.6330 |
| gross_win_rate | 0.3866 |
| sharpe_ratio | -5.9491 |
| sortino_ratio | -2.0367 |
| max_drawdown | 0.9098 |
| cagr | -0.6109 |
| net_avg_win | 33.6799 |
| net_avg_loss | -46.6212 |
| avg_hold_time_bars | 7.4588 |
| exposure | 0.1973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
