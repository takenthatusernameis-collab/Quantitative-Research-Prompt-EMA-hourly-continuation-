# EMA Hourly Continuation — WIF/USDT P20_21

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.2236 |
| net_win_rate | 0.3131 |
| gross_profit_factor | 0.6108 |
| gross_win_rate | 0.3504 |
| sharpe_ratio | -17.0526 |
| sortino_ratio | -8.9052 |
| max_drawdown | 1.0000 |
| cagr | -0.9935 |
| net_avg_win | 7.4603 |
| net_avg_loss | -15.2062 |
| avg_hold_time_bars | 1.5126 |
| exposure | 0.0848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
