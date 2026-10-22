# EMA Hourly Continuation — DASH/USDT P8_144

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.5311 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -4.2942 |
| sortino_ratio | -1.4115 |
| max_drawdown | 0.8348 |
| cagr | -0.5009 |
| net_avg_win | 36.3711 |
| net_avg_loss | -59.0639 |
| avg_hold_time_bars | 28.7207 |
| exposure | 0.7245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
