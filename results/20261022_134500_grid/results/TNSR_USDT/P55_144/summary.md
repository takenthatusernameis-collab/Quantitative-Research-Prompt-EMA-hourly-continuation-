# EMA Hourly Continuation — TNSR/USDT P55_144

**Symbol:** TNSR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6244 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8920 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -3.6460 |
| sortino_ratio | -1.1823 |
| max_drawdown | 0.7574 |
| cagr | -0.4253 |
| net_avg_win | 52.3507 |
| net_avg_loss | -69.5778 |
| avg_hold_time_bars | 11.1765 |
| exposure | 0.2666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
