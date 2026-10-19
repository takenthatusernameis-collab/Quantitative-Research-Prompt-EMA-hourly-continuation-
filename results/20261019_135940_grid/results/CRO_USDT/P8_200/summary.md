# EMA Hourly Continuation — CRO/USDT P8_200

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.5923 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9952 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -2.6882 |
| sortino_ratio | -0.7083 |
| max_drawdown | 0.5887 |
| cagr | -0.2907 |
| net_avg_win | 49.3802 |
| net_avg_loss | -77.0311 |
| avg_hold_time_bars | 50.5706 |
| exposure | 0.8137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
