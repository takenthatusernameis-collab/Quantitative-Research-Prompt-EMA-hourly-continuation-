# EMA Hourly Continuation — LQTY/USDT P89_144

**Symbol:** LQTY/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6278 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8346 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -2.7537 |
| sortino_ratio | -0.7182 |
| max_drawdown | 0.5681 |
| cagr | -0.2805 |
| net_avg_win | 62.1978 |
| net_avg_loss | -82.3768 |
| avg_hold_time_bars | 7.0267 |
| exposure | 0.1072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
