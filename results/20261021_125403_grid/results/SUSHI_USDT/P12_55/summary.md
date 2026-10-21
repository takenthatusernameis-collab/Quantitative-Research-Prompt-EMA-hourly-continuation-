# EMA Hourly Continuation — SUSHI/USDT P12_55

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.7511 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.7193 |
| sortino_ratio | -0.9606 |
| max_drawdown | 0.6808 |
| cagr | -0.3570 |
| net_avg_win | 68.9427 |
| net_avg_loss | -83.8096 |
| avg_hold_time_bars | 13.1445 |
| exposure | 0.3664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
