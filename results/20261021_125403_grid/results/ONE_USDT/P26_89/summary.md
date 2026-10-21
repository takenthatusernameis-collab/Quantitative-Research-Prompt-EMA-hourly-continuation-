# EMA Hourly Continuation — ONE/USDT P26_89

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8068 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9960 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.4487 |
| sortino_ratio | -0.4448 |
| max_drawdown | 0.4351 |
| cagr | -0.1860 |
| net_avg_win | 73.3027 |
| net_avg_loss | -90.8510 |
| avg_hold_time_bars | 16.1000 |
| exposure | 0.3366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
