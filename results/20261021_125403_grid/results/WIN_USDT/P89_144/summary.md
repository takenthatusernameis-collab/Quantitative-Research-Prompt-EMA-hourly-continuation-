# EMA Hourly Continuation — WIN/USDT P89_144

**Symbol:** WIN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.6379 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9701 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -2.0691 |
| sortino_ratio | -0.4596 |
| max_drawdown | 0.4354 |
| cagr | -0.1896 |
| net_avg_win | 61.2388 |
| net_avg_loss | -94.4005 |
| avg_hold_time_bars | 8.5210 |
| exposure | 0.0922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
