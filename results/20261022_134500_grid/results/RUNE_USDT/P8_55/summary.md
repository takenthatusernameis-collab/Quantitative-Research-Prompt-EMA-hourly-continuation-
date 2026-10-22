# EMA Hourly Continuation — RUNE/USDT P8_55

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1032 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 1.0169 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -5.8944 |
| sortino_ratio | -2.6461 |
| max_drawdown | 0.9629 |
| cagr | -0.7271 |
| net_avg_win | 30.9898 |
| net_avg_loss | -45.9012 |
| avg_hold_time_bars | 10.3711 |
| exposure | 0.4865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
