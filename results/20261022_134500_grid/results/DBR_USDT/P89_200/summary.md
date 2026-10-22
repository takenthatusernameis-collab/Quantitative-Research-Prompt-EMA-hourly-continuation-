# EMA Hourly Continuation — DBR/USDT P89_200

**Symbol:** DBR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.3896 |
| net_win_rate | 0.4027 |
| gross_profit_factor | 0.7062 |
| gross_win_rate | 0.4198 |
| sharpe_ratio | -5.2247 |
| sortino_ratio | -1.4037 |
| max_drawdown | 0.7558 |
| cagr | -0.5013 |
| net_avg_win | 40.7079 |
| net_avg_loss | -70.4499 |
| avg_hold_time_bars | 15.8259 |
| exposure | 0.2637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
