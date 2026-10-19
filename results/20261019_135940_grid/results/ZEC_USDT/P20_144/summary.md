# EMA Hourly Continuation — ZEC/USDT P20_144

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7655 |
| net_win_rate | 0.5188 |
| gross_profit_factor | 1.0726 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -1.6112 |
| sortino_ratio | -0.4991 |
| max_drawdown | 0.4958 |
| cagr | -0.2124 |
| net_avg_win | 59.1463 |
| net_avg_loss | -83.2806 |
| avg_hold_time_bars | 24.2875 |
| exposure | 0.5299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
