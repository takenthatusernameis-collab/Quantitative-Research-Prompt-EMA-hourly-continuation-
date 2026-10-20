# EMA Hourly Continuation — NOT/USDT P8_89

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6471 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9805 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -3.4545 |
| sortino_ratio | -1.1899 |
| max_drawdown | 0.7693 |
| cagr | -0.4379 |
| net_avg_win | 48.4688 |
| net_avg_loss | -71.6367 |
| avg_hold_time_bars | 25.9417 |
| exposure | 0.7104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
