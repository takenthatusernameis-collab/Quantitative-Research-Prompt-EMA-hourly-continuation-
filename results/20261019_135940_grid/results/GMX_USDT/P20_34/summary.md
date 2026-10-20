# EMA Hourly Continuation — GMX/USDT P20_34

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.3684 |
| net_win_rate | 0.3945 |
| gross_profit_factor | 0.8357 |
| gross_win_rate | 0.4164 |
| sharpe_ratio | -10.8088 |
| sortino_ratio | -5.1211 |
| max_drawdown | 0.9983 |
| cagr | -0.9204 |
| net_avg_win | 13.4138 |
| net_avg_loss | -23.7301 |
| avg_hold_time_bars | 3.4918 |
| exposure | 0.1746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
