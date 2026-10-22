# EMA Hourly Continuation — FET/USDT P50_200

**Symbol:** FET/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7080 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 0.9867 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.9072 |
| sortino_ratio | -0.5034 |
| max_drawdown | 0.4810 |
| cagr | -0.2152 |
| net_avg_win | 62.1098 |
| net_avg_loss | -88.2156 |
| avg_hold_time_bars | 24.8535 |
| exposure | 0.4010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
