# EMA Hourly Continuation — DOGE/USDT P34_200

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.8561 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0686 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -0.7064 |
| sortino_ratio | -0.1650 |
| max_drawdown | 0.2689 |
| cagr | -0.0745 |
| net_avg_win | 76.1874 |
| net_avg_loss | -97.4694 |
| avg_hold_time_bars | 41.3220 |
| exposure | 0.4959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
