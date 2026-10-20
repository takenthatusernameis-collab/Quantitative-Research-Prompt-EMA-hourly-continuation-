# EMA Hourly Continuation — GLM/USDT P8_34

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1285 |
| net_profit_factor | 0.5019 |
| net_win_rate | 0.4482 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -8.0879 |
| sortino_ratio | -4.0882 |
| max_drawdown | 0.9932 |
| cagr | -0.8623 |
| net_avg_win | 17.3704 |
| net_avg_loss | -28.1193 |
| avg_hold_time_bars | 6.2304 |
| exposure | 0.3639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
