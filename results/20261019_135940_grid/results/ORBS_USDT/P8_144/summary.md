# EMA Hourly Continuation — ORBS/USDT P8_144

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.5517 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.9081 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -5.4793 |
| sortino_ratio | -1.9237 |
| max_drawdown | 0.9057 |
| cagr | -0.6072 |
| net_avg_win | 41.0676 |
| net_avg_loss | -56.5061 |
| avg_hold_time_bars | 25.2022 |
| exposure | 0.7194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
