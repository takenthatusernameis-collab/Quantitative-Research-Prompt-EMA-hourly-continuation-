# EMA Hourly Continuation — DCR/USDT P20_50

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1035 |
| net_profit_factor | 0.4406 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.8081 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -8.3203 |
| sortino_ratio | -3.7737 |
| max_drawdown | 0.9911 |
| cagr | -0.8432 |
| net_avg_win | 17.7758 |
| net_avg_loss | -29.7151 |
| avg_hold_time_bars | 5.2850 |
| exposure | 0.2475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
