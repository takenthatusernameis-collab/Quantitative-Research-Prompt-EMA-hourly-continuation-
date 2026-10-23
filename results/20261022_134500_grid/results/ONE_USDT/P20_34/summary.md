# EMA Hourly Continuation — ONE/USDT P20_34

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1195 |
| net_profit_factor | 0.4116 |
| net_win_rate | 0.4176 |
| gross_profit_factor | 0.8441 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -10.6466 |
| sortino_ratio | -5.2115 |
| max_drawdown | 0.9988 |
| cagr | -0.9302 |
| net_avg_win | 14.0013 |
| net_avg_loss | -24.3881 |
| avg_hold_time_bars | 2.6218 |
| exposure | 0.1424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
