# EMA Hourly Continuation — API3/USDT P34_55

**Symbol:** API3/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7657 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0706 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -1.7491 |
| sortino_ratio | -0.4848 |
| max_drawdown | 0.4851 |
| cagr | -0.1995 |
| net_avg_win | 73.2331 |
| net_avg_loss | -101.4921 |
| avg_hold_time_bars | 6.2264 |
| exposure | 0.1050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
