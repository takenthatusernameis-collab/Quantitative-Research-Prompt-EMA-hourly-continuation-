# EMA Hourly Continuation — OGN/USDT P26_200

**Symbol:** OGN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7027 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8802 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -2.0081 |
| sortino_ratio | -0.5100 |
| max_drawdown | 0.4870 |
| cagr | -0.2100 |
| net_avg_win | 70.6248 |
| net_avg_loss | -87.6545 |
| avg_hold_time_bars | 38.6615 |
| exposure | 0.5633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
