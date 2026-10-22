# EMA Hourly Continuation — FIDA/USDT P12_26

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.6414 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9053 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -3.3321 |
| sortino_ratio | -1.1902 |
| max_drawdown | 0.7499 |
| cagr | -0.4205 |
| net_avg_win | 44.4200 |
| net_avg_loss | -64.1408 |
| avg_hold_time_bars | 6.2173 |
| exposure | 0.1761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
