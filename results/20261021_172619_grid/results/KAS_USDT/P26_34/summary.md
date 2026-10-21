# EMA Hourly Continuation — KAS/USDT P26_34

**Symbol:** KAS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.9378 |
| net_win_rate | 0.5725 |
| gross_profit_factor | 1.3280 |
| gross_win_rate | 0.5725 |
| sharpe_ratio | -0.2078 |
| sortino_ratio | -0.0357 |
| max_drawdown | 0.1561 |
| cagr | -0.0178 |
| net_avg_win | 84.4409 |
| net_avg_loss | -120.5603 |
| avg_hold_time_bars | 5.1304 |
| exposure | 0.0322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
