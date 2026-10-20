# EMA Hourly Continuation — RIO/USDT P100_144

**Symbol:** RIO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.4267 |
| net_win_rate | 0.4059 |
| gross_profit_factor | 0.6671 |
| gross_win_rate | 0.4076 |
| sharpe_ratio | -6.1945 |
| sortino_ratio | -2.1113 |
| max_drawdown | 0.9240 |
| cagr | -0.6413 |
| net_avg_win | 29.1945 |
| net_avg_loss | -46.7420 |
| avg_hold_time_bars | 3.5596 |
| exposure | 0.0946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
