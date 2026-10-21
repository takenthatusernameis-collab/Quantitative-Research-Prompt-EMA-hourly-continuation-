# EMA Hourly Continuation — KSM/USDT P20_144

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6909 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8599 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -2.2673 |
| sortino_ratio | -0.5939 |
| max_drawdown | 0.5257 |
| cagr | -0.2400 |
| net_avg_win | 70.8956 |
| net_avg_loss | -87.5569 |
| avg_hold_time_bars | 38.3666 |
| exposure | 0.5947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
