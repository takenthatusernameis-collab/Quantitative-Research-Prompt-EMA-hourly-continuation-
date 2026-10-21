# EMA Hourly Continuation — REQ/USDT P50_200

**Symbol:** REQ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.5555 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.7905 |
| gross_win_rate | 0.4205 |
| sharpe_ratio | -4.2223 |
| sortino_ratio | -1.1838 |
| max_drawdown | 0.7678 |
| cagr | -0.4239 |
| net_avg_win | 57.4804 |
| net_avg_loss | -74.2975 |
| avg_hold_time_bars | 18.2103 |
| exposure | 0.3228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
