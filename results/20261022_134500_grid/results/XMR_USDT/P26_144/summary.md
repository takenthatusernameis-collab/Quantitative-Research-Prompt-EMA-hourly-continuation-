# EMA Hourly Continuation — XMR/USDT P26_144

**Symbol:** XMR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 817 |
| net_profit_factor | 0.4607 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.8366 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -6.7959 |
| sortino_ratio | -2.7103 |
| max_drawdown | 0.9670 |
| cagr | -0.7417 |
| net_avg_win | 23.0612 |
| net_avg_loss | -39.0454 |
| avg_hold_time_bars | 11.2460 |
| exposure | 0.4176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
