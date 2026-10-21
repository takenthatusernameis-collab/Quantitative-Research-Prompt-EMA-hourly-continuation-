# EMA Hourly Continuation — PEOPLE/USDT P12_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.9024 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0382 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -0.4974 |
| sortino_ratio | -0.1200 |
| max_drawdown | 0.2349 |
| cagr | -0.0567 |
| net_avg_win | 87.2658 |
| net_avg_loss | -100.8775 |
| avg_hold_time_bars | 58.8063 |
| exposure | 0.7557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
