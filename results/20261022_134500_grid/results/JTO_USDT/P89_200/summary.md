# EMA Hourly Continuation — JTO/USDT P89_200

**Symbol:** JTO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6000 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8323 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -3.2179 |
| sortino_ratio | -0.9416 |
| max_drawdown | 0.6745 |
| cagr | -0.3540 |
| net_avg_win | 51.7724 |
| net_avg_loss | -71.7849 |
| avg_hold_time_bars | 9.6000 |
| exposure | 0.1855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
