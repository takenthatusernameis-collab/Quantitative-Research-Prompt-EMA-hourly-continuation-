# EMA Hourly Continuation — AGLD/USDT P12_100

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.7013 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -2.8254 |
| sortino_ratio | -0.9952 |
| max_drawdown | 0.7012 |
| cagr | -0.3747 |
| net_avg_win | 53.4247 |
| net_avg_loss | -72.8361 |
| avg_hold_time_bars | 20.6747 |
| exposure | 0.5838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
