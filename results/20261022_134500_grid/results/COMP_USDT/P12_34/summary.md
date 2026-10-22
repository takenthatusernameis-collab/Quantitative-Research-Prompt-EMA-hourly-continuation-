# EMA Hourly Continuation — COMP/USDT P12_34

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1313 |
| net_profit_factor | 0.3852 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -9.6302 |
| sortino_ratio | -4.9238 |
| max_drawdown | 0.9978 |
| cagr | -0.9130 |
| net_avg_win | 10.7966 |
| net_avg_loss | -22.1110 |
| avg_hold_time_bars | 4.7281 |
| exposure | 0.2822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
