# EMA Hourly Continuation — BSV/USDT P34_55

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.5245 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7867 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -3.6802 |
| sortino_ratio | -0.9987 |
| max_drawdown | 0.6876 |
| cagr | -0.3665 |
| net_avg_win | 47.0340 |
| net_avg_loss | -71.7369 |
| avg_hold_time_bars | 6.5278 |
| exposure | 0.1068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
