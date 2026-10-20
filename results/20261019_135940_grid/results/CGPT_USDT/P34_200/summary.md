# EMA Hourly Continuation — CGPT/USDT P34_200

**Symbol:** CGPT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6766 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9512 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.6689 |
| sortino_ratio | -0.7450 |
| max_drawdown | 0.6021 |
| cagr | -0.3039 |
| net_avg_win | 65.4227 |
| net_avg_loss | -88.7929 |
| avg_hold_time_bars | 25.7920 |
| exposure | 0.4678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
