# EMA Hourly Continuation — SEI/USDT P21_34

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.6694 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.2284 |
| sortino_ratio | -0.5296 |
| max_drawdown | 0.4762 |
| cagr | -0.2148 |
| net_avg_win | 70.9087 |
| net_avg_loss | -94.3155 |
| avg_hold_time_bars | 4.7283 |
| exposure | 0.0593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
