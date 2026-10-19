# EMA Hourly Continuation — APT/USDT P20_21

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1232 |
| net_profit_factor | 0.1107 |
| net_win_rate | 0.2760 |
| gross_profit_factor | 0.5963 |
| gross_win_rate | 0.3401 |
| sharpe_ratio | -19.1088 |
| sortino_ratio | -10.3750 |
| max_drawdown | 1.0000 |
| cagr | -0.9975 |
| net_avg_win | 3.6619 |
| net_avg_loss | -12.6066 |
| avg_hold_time_bars | 1.5414 |
| exposure | 0.0863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
