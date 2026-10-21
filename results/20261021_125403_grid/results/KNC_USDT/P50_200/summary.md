# EMA Hourly Continuation — KNC/USDT P50_200

**Symbol:** KNC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7742 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 1.0190 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -1.4845 |
| sortino_ratio | -0.3724 |
| max_drawdown | 0.4053 |
| cagr | -0.1577 |
| net_avg_win | 77.9360 |
| net_avg_loss | -101.3264 |
| avg_hold_time_bars | 29.4853 |
| exposure | 0.4115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
