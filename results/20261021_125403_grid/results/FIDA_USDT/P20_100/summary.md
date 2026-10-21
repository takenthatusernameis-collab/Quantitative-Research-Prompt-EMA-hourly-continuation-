# EMA Hourly Continuation — FIDA/USDT P20_100

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8580 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -2.3880 |
| sortino_ratio | -0.7496 |
| max_drawdown | 0.6099 |
| cagr | -0.2918 |
| net_avg_win | 51.6154 |
| net_avg_loss | -69.4799 |
| avg_hold_time_bars | 20.0287 |
| exposure | 0.4423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
