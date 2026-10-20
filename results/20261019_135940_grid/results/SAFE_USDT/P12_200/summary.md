# EMA Hourly Continuation — SAFE/USDT P12_200

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7129 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -2.0866 |
| sortino_ratio | -0.5735 |
| max_drawdown | 0.5174 |
| cagr | -0.2419 |
| net_avg_win | 66.2125 |
| net_avg_loss | -89.5211 |
| avg_hold_time_bars | 42.2730 |
| exposure | 0.7376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
