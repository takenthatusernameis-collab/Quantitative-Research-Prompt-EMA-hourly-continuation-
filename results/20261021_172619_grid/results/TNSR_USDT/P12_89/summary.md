# EMA Hourly Continuation — TNSR/USDT P12_89

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.8218 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.6078 |
| sortino_ratio | -0.5402 |
| max_drawdown | 0.5220 |
| cagr | -0.2220 |
| net_avg_win | 78.6852 |
| net_avg_loss | -93.6977 |
| avg_hold_time_bars | 20.7428 |
| exposure | 0.5219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
