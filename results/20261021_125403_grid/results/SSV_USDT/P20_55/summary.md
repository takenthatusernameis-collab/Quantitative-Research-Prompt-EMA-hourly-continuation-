# EMA Hourly Continuation — SSV/USDT P20_55

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.7109 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9151 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -3.0016 |
| sortino_ratio | -1.0426 |
| max_drawdown | 0.7155 |
| cagr | -0.3808 |
| net_avg_win | 61.8319 |
| net_avg_loss | -76.3083 |
| avg_hold_time_bars | 8.5394 |
| exposure | 0.2307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
