# EMA Hourly Continuation — CRV/USDT P26_200

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.8489 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -0.9299 |
| sortino_ratio | -0.2314 |
| max_drawdown | 0.3151 |
| cagr | -0.1028 |
| net_avg_win | 88.1128 |
| net_avg_loss | -105.1836 |
| avg_hold_time_bars | 41.3775 |
| exposure | 0.5680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
