# EMA Hourly Continuation — CATI/USDT P20_89

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6552 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8066 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -2.7657 |
| sortino_ratio | -0.8426 |
| max_drawdown | 0.5930 |
| cagr | -0.3229 |
| net_avg_win | 60.7206 |
| net_avg_loss | -77.1575 |
| avg_hold_time_bars | 19.1880 |
| exposure | 0.4028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
