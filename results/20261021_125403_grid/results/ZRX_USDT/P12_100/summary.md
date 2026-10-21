# EMA Hourly Continuation — ZRX/USDT P12_100

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7445 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.1534 |
| sortino_ratio | -0.7000 |
| max_drawdown | 0.5712 |
| cagr | -0.2758 |
| net_avg_win | 63.7196 |
| net_avg_loss | -82.0314 |
| avg_hold_time_bars | 24.0173 |
| exposure | 0.5666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
