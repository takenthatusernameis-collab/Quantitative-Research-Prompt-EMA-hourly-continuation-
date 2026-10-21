# EMA Hourly Continuation — MNT/USDT P20_144

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.9223 |
| net_win_rate | 0.5414 |
| gross_profit_factor | 1.1636 |
| gross_win_rate | 0.5414 |
| sharpe_ratio | -0.3935 |
| sortino_ratio | -0.1044 |
| max_drawdown | 0.2415 |
| cagr | -0.0511 |
| net_avg_win | 80.0532 |
| net_avg_loss | -102.4796 |
| avg_hold_time_bars | 37.6361 |
| exposure | 0.5782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
