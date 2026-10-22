# EMA Hourly Continuation — MOCA/USDT P34_144

**Symbol:** MOCA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8291 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0236 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.0412 |
| sortino_ratio | -0.2755 |
| max_drawdown | 0.2738 |
| cagr | -0.1212 |
| net_avg_win | 78.2865 |
| net_avg_loss | -98.1492 |
| avg_hold_time_bars | 26.9387 |
| exposure | 0.4186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
