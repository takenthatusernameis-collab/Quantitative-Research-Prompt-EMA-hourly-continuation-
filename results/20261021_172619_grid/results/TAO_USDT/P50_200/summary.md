# EMA Hourly Continuation — TAO/USDT P50_200

**Symbol:** TAO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8385 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -0.8419 |
| sortino_ratio | -0.1997 |
| max_drawdown | 0.2605 |
| cagr | -0.0893 |
| net_avg_win | 79.2941 |
| net_avg_loss | -93.8845 |
| avg_hold_time_bars | 27.0727 |
| exposure | 0.3384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
