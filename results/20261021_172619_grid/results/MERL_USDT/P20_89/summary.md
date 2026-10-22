# EMA Hourly Continuation — MERL/USDT P20_89

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.8090 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9561 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -1.5150 |
| sortino_ratio | -0.4696 |
| max_drawdown | 0.4851 |
| cagr | -0.1958 |
| net_avg_win | 77.8064 |
| net_avg_loss | -91.0092 |
| avg_hold_time_bars | 18.1401 |
| exposure | 0.3894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
