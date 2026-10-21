# EMA Hourly Continuation — ETN/USDT P20_26

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.3980 |
| net_win_rate | 0.3636 |
| gross_profit_factor | 0.5450 |
| gross_win_rate | 0.3636 |
| sharpe_ratio | -4.1222 |
| sortino_ratio | -0.8959 |
| max_drawdown | 0.5909 |
| cagr | -0.3434 |
| net_avg_win | 53.8948 |
| net_avg_loss | -77.3746 |
| avg_hold_time_bars | 5.9394 |
| exposure | 0.0639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
