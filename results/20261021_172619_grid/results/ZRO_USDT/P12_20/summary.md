# EMA Hourly Continuation — ZRO/USDT P12_20

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.8355 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0791 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -0.8537 |
| sortino_ratio | -0.1849 |
| max_drawdown | 0.3115 |
| cagr | -0.0822 |
| net_avg_win | 84.5030 |
| net_avg_loss | -109.1569 |
| avg_hold_time_bars | 4.5286 |
| exposure | 0.0465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
