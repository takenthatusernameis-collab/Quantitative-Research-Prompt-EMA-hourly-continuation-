# EMA Hourly Continuation — PUFFER/USDT P144_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.4788 |
| net_win_rate | 0.4158 |
| gross_profit_factor | 0.7517 |
| gross_win_rate | 0.4192 |
| sharpe_ratio | -4.4861 |
| sortino_ratio | -1.2086 |
| max_drawdown | 0.6941 |
| cagr | -0.4366 |
| net_avg_win | 52.0570 |
| net_avg_loss | -77.3857 |
| avg_hold_time_bars | 5.0344 |
| exposure | 0.0829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
