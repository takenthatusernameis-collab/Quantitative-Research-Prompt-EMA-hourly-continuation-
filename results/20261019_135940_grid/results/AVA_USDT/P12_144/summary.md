# EMA Hourly Continuation — AVA/USDT P12_144

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.5771 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8722 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -3.5197 |
| sortino_ratio | -1.1546 |
| max_drawdown | 0.7662 |
| cagr | -0.4318 |
| net_avg_win | 39.6357 |
| net_avg_loss | -60.7694 |
| avg_hold_time_bars | 23.9622 |
| exposure | 0.6056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
