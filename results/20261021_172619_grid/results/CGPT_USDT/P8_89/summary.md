# EMA Hourly Continuation — CGPT/USDT P8_89

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.9900 |
| net_win_rate | 0.5462 |
| gross_profit_factor | 1.1906 |
| gross_win_rate | 0.5462 |
| sharpe_ratio | 0.0006 |
| sortino_ratio | 0.0002 |
| max_drawdown | 0.1539 |
| cagr | -0.0102 |
| net_avg_win | 88.4168 |
| net_avg_loss | -107.4752 |
| avg_hold_time_bars | 26.1712 |
| exposure | 0.6186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
