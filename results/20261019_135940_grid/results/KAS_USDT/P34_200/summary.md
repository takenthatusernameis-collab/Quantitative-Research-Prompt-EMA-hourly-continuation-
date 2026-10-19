# EMA Hourly Continuation — KAS/USDT P34_200

**Symbol:** KAS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.5611 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -3.6389 |
| sortino_ratio | -1.0684 |
| max_drawdown | 0.7440 |
| cagr | -0.4077 |
| net_avg_win | 45.1811 |
| net_avg_loss | -70.0358 |
| avg_hold_time_bars | 20.5775 |
| exposure | 0.4162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
