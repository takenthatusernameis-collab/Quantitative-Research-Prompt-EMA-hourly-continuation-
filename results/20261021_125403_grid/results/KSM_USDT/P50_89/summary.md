# EMA Hourly Continuation — KSM/USDT P50_89

**Symbol:** KSM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7179 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0021 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0132 |
| sortino_ratio | -0.5516 |
| max_drawdown | 0.4909 |
| cagr | -0.2224 |
| net_avg_win | 65.4830 |
| net_avg_loss | -91.2167 |
| avg_hold_time_bars | 7.2967 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
