# EMA Hourly Continuation — DIA/USDT P12_55

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.6960 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9011 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -3.1755 |
| sortino_ratio | -1.1760 |
| max_drawdown | 0.7658 |
| cagr | -0.4176 |
| net_avg_win | 53.4175 |
| net_avg_loss | -68.0087 |
| avg_hold_time_bars | 10.8085 |
| exposure | 0.3321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
