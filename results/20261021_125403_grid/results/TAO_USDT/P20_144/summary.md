# EMA Hourly Continuation — TAO/USDT P20_144

**Symbol:** TAO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8900 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0258 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -0.6933 |
| sortino_ratio | -0.1875 |
| max_drawdown | 0.3050 |
| cagr | -0.0859 |
| net_avg_win | 90.8011 |
| net_avg_loss | -104.3404 |
| avg_hold_time_bars | 32.9326 |
| exposure | 0.5329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
