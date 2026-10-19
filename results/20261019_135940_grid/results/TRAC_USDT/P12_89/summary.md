# EMA Hourly Continuation — TRAC/USDT P12_89

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4849 |
| gross_profit_factor | 1.0016 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -3.5124 |
| sortino_ratio | -1.3376 |
| max_drawdown | 0.8067 |
| cagr | -0.4698 |
| net_avg_win | 48.6592 |
| net_avg_loss | -67.0025 |
| avg_hold_time_bars | 13.8849 |
| exposure | 0.4607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
