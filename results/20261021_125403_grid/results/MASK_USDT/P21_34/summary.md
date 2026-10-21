# EMA Hourly Continuation — MASK/USDT P21_34

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.5954 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9514 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -3.4889 |
| sortino_ratio | -1.0548 |
| max_drawdown | 0.7105 |
| cagr | -0.3870 |
| net_avg_win | 48.1919 |
| net_avg_loss | -76.0140 |
| avg_hold_time_bars | 5.5000 |
| exposure | 0.1115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
