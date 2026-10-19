# EMA Hourly Continuation — JUP/USDT P50_144

**Symbol:** JUP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5507 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8400 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -4.0690 |
| sortino_ratio | -1.3019 |
| max_drawdown | 0.7993 |
| cagr | -0.4661 |
| net_avg_win | 40.6815 |
| net_avg_loss | -62.8273 |
| avg_hold_time_bars | 10.2096 |
| exposure | 0.2413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
