# EMA Hourly Continuation — INJ/USDT P26_89

**Symbol:** INJ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.8614 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0600 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.0273 |
| sortino_ratio | -0.3202 |
| max_drawdown | 0.3609 |
| cagr | -0.1393 |
| net_avg_win | 80.6266 |
| net_avg_loss | -99.3454 |
| avg_hold_time_bars | 11.8894 |
| exposure | 0.2540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
