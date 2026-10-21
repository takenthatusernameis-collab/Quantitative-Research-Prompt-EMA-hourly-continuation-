# EMA Hourly Continuation — GMX/USDT P21_200

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8120 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9827 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -1.4109 |
| sortino_ratio | -0.3983 |
| max_drawdown | 0.4885 |
| cagr | -0.1686 |
| net_avg_win | 83.0409 |
| net_avg_loss | -99.1841 |
| avg_hold_time_bars | 32.2500 |
| exposure | 0.5746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
