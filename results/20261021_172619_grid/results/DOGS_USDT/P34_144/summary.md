# EMA Hourly Continuation — DOGS/USDT P34_144

**Symbol:** DOGS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.8778 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0495 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -0.8143 |
| sortino_ratio | -0.2151 |
| max_drawdown | 0.3354 |
| cagr | -0.0966 |
| net_avg_win | 95.2456 |
| net_avg_loss | -113.0933 |
| avg_hold_time_bars | 26.9793 |
| exposure | 0.4151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
