# EMA Hourly Continuation — CFG/USDT P55_200

**Symbol:** CFG/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6316 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -2.6905 |
| sortino_ratio | -0.8011 |
| max_drawdown | 0.6290 |
| cagr | -0.3132 |
| net_avg_win | 50.5718 |
| net_avg_loss | -69.0651 |
| avg_hold_time_bars | 15.4877 |
| exposure | 0.3147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
