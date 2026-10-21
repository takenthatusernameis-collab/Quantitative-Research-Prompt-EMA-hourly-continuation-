# EMA Hourly Continuation — ENJ/USDT P21_55

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.5050 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.9136 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -7.3763 |
| sortino_ratio | -3.2424 |
| max_drawdown | 0.9820 |
| cagr | -0.7936 |
| net_avg_win | 23.2795 |
| net_avg_loss | -36.7099 |
| avg_hold_time_bars | 5.0216 |
| exposure | 0.2204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
