# EMA Hourly Continuation — IMX/USDT P12_20

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7547 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0339 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.6849 |
| sortino_ratio | -0.4313 |
| max_drawdown | 0.4457 |
| cagr | -0.1800 |
| net_avg_win | 75.2622 |
| net_avg_loss | -101.6140 |
| avg_hold_time_bars | 4.8025 |
| exposure | 0.0693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
