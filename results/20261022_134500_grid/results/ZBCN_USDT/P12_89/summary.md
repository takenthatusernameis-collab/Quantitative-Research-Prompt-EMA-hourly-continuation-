# EMA Hourly Continuation — ZBCN/USDT P12_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 929 |
| net_profit_factor | 0.6757 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -3.8479 |
| sortino_ratio | -1.6659 |
| max_drawdown | 0.8660 |
| cagr | -0.5489 |
| net_avg_win | 39.6325 |
| net_avg_loss | -55.5782 |
| avg_hold_time_bars | 11.0635 |
| exposure | 0.4755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
