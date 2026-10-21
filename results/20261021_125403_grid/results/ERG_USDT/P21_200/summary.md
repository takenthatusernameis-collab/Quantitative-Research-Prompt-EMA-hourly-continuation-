# EMA Hourly Continuation — ERG/USDT P21_200

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7667 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9258 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.3926 |
| sortino_ratio | -0.3637 |
| max_drawdown | 0.3684 |
| cagr | -0.1549 |
| net_avg_win | 69.4727 |
| net_avg_loss | -85.8757 |
| avg_hold_time_bars | 37.1343 |
| exposure | 0.5655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
