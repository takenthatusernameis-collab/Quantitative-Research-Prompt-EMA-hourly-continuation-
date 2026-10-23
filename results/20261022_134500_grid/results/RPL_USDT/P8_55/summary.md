# EMA Hourly Continuation — RPL/USDT P8_55

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.6444 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -4.4007 |
| sortino_ratio | -1.8519 |
| max_drawdown | 0.8975 |
| cagr | -0.5872 |
| net_avg_win | 37.7875 |
| net_avg_loss | -53.2898 |
| avg_hold_time_bars | 12.7953 |
| exposure | 0.5206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
