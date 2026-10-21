# EMA Hourly Continuation — SNX/USDT P12_144

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.8500 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0204 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.0536 |
| sortino_ratio | -0.3109 |
| max_drawdown | 0.3331 |
| cagr | -0.1358 |
| net_avg_win | 81.1896 |
| net_avg_loss | -97.3237 |
| avg_hold_time_bars | 32.4460 |
| exposure | 0.6255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
