# EMA Hourly Continuation — BTT/USDT P12_89

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.6384 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -3.3702 |
| sortino_ratio | -0.9962 |
| max_drawdown | 0.7105 |
| cagr | -0.3723 |
| net_avg_win | 60.2562 |
| net_avg_loss | -83.2594 |
| avg_hold_time_bars | 30.5058 |
| exposure | 0.5976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
