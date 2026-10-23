# EMA Hourly Continuation — CKB/USDT P144_200

**Symbol:** CKB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5937 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.0811 |
| gross_win_rate | 0.5332 |
| sharpe_ratio | -2.9892 |
| sortino_ratio | -0.8638 |
| max_drawdown | 0.6567 |
| cagr | -0.3316 |
| net_avg_win | 43.2533 |
| net_avg_loss | -81.5790 |
| avg_hold_time_bars | 4.3096 |
| exposure | 0.0797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
