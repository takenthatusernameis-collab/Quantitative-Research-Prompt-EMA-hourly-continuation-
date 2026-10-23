# EMA Hourly Continuation — MOG/USDT P12_34

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1161 |
| net_profit_factor | 0.7022 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -5.5856 |
| sortino_ratio | -2.8206 |
| max_drawdown | 0.9526 |
| cagr | -0.7351 |
| net_avg_win | 40.6212 |
| net_avg_loss | -52.6150 |
| avg_hold_time_bars | 4.5736 |
| exposure | 0.2640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
