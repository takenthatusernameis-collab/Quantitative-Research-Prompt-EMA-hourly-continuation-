# EMA Hourly Continuation — SKY/USDT P20_50

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 803 |
| net_profit_factor | 0.4537 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -7.3932 |
| sortino_ratio | -3.2698 |
| max_drawdown | 0.9623 |
| cagr | -0.7985 |
| net_avg_win | 21.8981 |
| net_avg_loss | -40.2195 |
| avg_hold_time_bars | 5.0274 |
| exposure | 0.2251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
