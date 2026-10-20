# EMA Hourly Continuation — REQ/USDT P21_144

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.5276 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -6.6676 |
| sortino_ratio | -2.4435 |
| max_drawdown | 0.9533 |
| cagr | -0.7009 |
| net_avg_win | 36.7750 |
| net_avg_loss | -52.0550 |
| avg_hold_time_bars | 16.3254 |
| exposure | 0.5016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
