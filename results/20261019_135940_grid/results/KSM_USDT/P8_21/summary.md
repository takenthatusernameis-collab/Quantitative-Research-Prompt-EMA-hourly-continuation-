# EMA Hourly Continuation — KSM/USDT P8_21

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1631 |
| net_profit_factor | 0.3507 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.8212 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -11.7800 |
| sortino_ratio | -6.6975 |
| max_drawdown | 0.9998 |
| cagr | -0.9656 |
| net_avg_win | 7.7370 |
| net_avg_loss | -16.5041 |
| avg_hold_time_bars | 3.2918 |
| exposure | 0.2440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
