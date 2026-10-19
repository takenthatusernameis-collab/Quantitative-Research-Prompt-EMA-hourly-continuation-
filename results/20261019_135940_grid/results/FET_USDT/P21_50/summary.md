# EMA Hourly Continuation — FET/USDT P21_50

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1017 |
| net_profit_factor | 0.4276 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.7031 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -7.7419 |
| sortino_ratio | -3.4711 |
| max_drawdown | 0.9860 |
| cagr | -0.8174 |
| net_avg_win | 16.7047 |
| net_avg_loss | -29.9078 |
| avg_hold_time_bars | 4.2812 |
| exposure | 0.1979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
