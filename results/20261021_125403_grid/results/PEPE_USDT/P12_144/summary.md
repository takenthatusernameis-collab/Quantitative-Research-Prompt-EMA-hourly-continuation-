# EMA Hourly Continuation — PEPE/USDT P12_144

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.9142 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.0864 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -0.5090 |
| sortino_ratio | -0.1335 |
| max_drawdown | 0.2288 |
| cagr | -0.0631 |
| net_avg_win | 92.9829 |
| net_avg_loss | -110.6689 |
| avg_hold_time_bars | 45.1205 |
| exposure | 0.6809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
