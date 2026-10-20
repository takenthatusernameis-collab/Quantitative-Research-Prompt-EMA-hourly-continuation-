# EMA Hourly Continuation — SATS/USDT P8_34

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9944 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -5.2381 |
| sortino_ratio | -2.4964 |
| max_drawdown | 0.9540 |
| cagr | -0.6976 |
| net_avg_win | 29.9721 |
| net_avg_loss | -42.9390 |
| avg_hold_time_bars | 6.8854 |
| exposure | 0.3589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
