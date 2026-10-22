# EMA Hourly Continuation — COTI/USDT P12_89

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.8563 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0200 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.1154 |
| sortino_ratio | -0.3720 |
| max_drawdown | 0.3966 |
| cagr | -0.1604 |
| net_avg_win | 77.3133 |
| net_avg_loss | -92.6509 |
| avg_hold_time_bars | 21.2865 |
| exposure | 0.5235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
