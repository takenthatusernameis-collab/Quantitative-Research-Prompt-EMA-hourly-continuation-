# EMA Hourly Continuation — SATS/USDT P26_34

**Symbol:** SATS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.6315 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -2.3216 |
| sortino_ratio | -0.4970 |
| max_drawdown | 0.4751 |
| cagr | -0.2074 |
| net_avg_win | 71.7208 |
| net_avg_loss | -99.4929 |
| avg_hold_time_bars | 5.2819 |
| exposure | 0.0543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
