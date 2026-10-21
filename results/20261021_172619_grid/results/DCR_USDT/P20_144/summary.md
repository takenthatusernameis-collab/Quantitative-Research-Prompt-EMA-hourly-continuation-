# EMA Hourly Continuation — DCR/USDT P20_144

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7725 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.5166 |
| sortino_ratio | -0.4703 |
| max_drawdown | 0.4811 |
| cagr | -0.1960 |
| net_avg_win | 60.1409 |
| net_avg_loss | -79.8526 |
| avg_hold_time_bars | 23.5127 |
| exposure | 0.5022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
