# EMA Hourly Continuation — TRADE/USDT P50_55

**Symbol:** TRADE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.1902 |
| net_win_rate | 0.2905 |
| gross_profit_factor | 0.5095 |
| gross_win_rate | 0.3082 |
| sharpe_ratio | -12.0191 |
| sortino_ratio | -4.4361 |
| max_drawdown | 0.9980 |
| cagr | -0.9149 |
| net_avg_win | 12.9469 |
| net_avg_loss | -27.8798 |
| avg_hold_time_bars | 3.3323 |
| exposure | 0.0944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
