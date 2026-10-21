# EMA Hourly Continuation — MANA/USDT P26_144

**Symbol:** MANA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8927 |
| net_win_rate | 0.5269 |
| gross_profit_factor | 1.1036 |
| gross_win_rate | 0.5269 |
| sharpe_ratio | -0.6423 |
| sortino_ratio | -0.1737 |
| max_drawdown | 0.2382 |
| cagr | -0.0799 |
| net_avg_win | 84.3709 |
| net_avg_loss | -105.2704 |
| avg_hold_time_bars | 30.2040 |
| exposure | 0.4846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
