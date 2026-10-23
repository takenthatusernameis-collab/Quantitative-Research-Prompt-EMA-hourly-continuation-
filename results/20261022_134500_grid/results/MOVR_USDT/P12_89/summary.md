# EMA Hourly Continuation — MOVR/USDT P12_89

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.5342 |
| net_win_rate | 0.4254 |
| gross_profit_factor | 0.8103 |
| gross_win_rate | 0.4344 |
| sharpe_ratio | -5.6742 |
| sortino_ratio | -2.2251 |
| max_drawdown | 0.9326 |
| cagr | -0.6539 |
| net_avg_win | 32.2298 |
| net_avg_loss | -44.6791 |
| avg_hold_time_bars | 15.3663 |
| exposure | 0.5434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
