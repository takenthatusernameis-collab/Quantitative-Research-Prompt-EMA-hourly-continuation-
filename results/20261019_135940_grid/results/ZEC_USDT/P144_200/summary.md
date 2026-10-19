# EMA Hourly Continuation — ZEC/USDT P144_200

**Symbol:** ZEC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.4988 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.8710 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -3.4069 |
| sortino_ratio | -0.9202 |
| max_drawdown | 0.6754 |
| cagr | -0.3566 |
| net_avg_win | 38.5155 |
| net_avg_loss | -69.2197 |
| avg_hold_time_bars | 4.4344 |
| exposure | 0.0738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
