# EMA Hourly Continuation — SEI/USDT P21_34

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1121 |
| net_profit_factor | 0.4382 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.8432 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -10.3358 |
| sortino_ratio | -4.9127 |
| max_drawdown | 0.9980 |
| cagr | -0.9158 |
| net_avg_win | 16.5268 |
| net_avg_loss | -27.3294 |
| avg_hold_time_bars | 2.3622 |
| exposure | 0.1204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
