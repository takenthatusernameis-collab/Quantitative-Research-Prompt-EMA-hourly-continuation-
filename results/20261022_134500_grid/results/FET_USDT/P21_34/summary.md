# EMA Hourly Continuation — FET/USDT P21_34

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1165 |
| net_profit_factor | 0.3827 |
| net_win_rate | 0.4034 |
| gross_profit_factor | 0.7363 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -10.7927 |
| sortino_ratio | -5.2432 |
| max_drawdown | 0.9987 |
| cagr | -0.9282 |
| net_avg_win | 13.1748 |
| net_avg_loss | -23.2787 |
| avg_hold_time_bars | 2.2609 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
