# EMA Hourly Continuation — ZEC/USDT P55_89

**Symbol:** ZEC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.8300 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0834 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -0.9471 |
| sortino_ratio | -0.2255 |
| max_drawdown | 0.3042 |
| cagr | -0.0988 |
| net_avg_win | 79.0986 |
| net_avg_loss | -103.2971 |
| avg_hold_time_bars | 5.7802 |
| exposure | 0.0717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
