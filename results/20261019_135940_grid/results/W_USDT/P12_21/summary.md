# EMA Hourly Continuation — W/USDT P12_21

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1463 |
| net_profit_factor | 0.4364 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -10.7818 |
| sortino_ratio | -5.8167 |
| max_drawdown | 0.9994 |
| cagr | -0.9466 |
| net_avg_win | 12.1484 |
| net_avg_loss | -21.4675 |
| avg_hold_time_bars | 2.3520 |
| exposure | 0.1564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
