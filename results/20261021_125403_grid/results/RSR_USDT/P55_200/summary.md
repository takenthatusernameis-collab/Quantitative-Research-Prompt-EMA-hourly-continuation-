# EMA Hourly Continuation — RSR/USDT P55_200

**Symbol:** RSR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.7968 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9405 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.1118 |
| sortino_ratio | -0.2761 |
| max_drawdown | 0.2807 |
| cagr | -0.1203 |
| net_avg_win | 72.8875 |
| net_avg_loss | -87.9156 |
| avg_hold_time_bars | 25.6192 |
| exposure | 0.3517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
