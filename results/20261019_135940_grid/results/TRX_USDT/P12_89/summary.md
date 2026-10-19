# EMA Hourly Continuation — TRX/USDT P12_89

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.4009 |
| net_win_rate | 0.4071 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -9.2032 |
| sortino_ratio | -3.4798 |
| max_drawdown | 0.9905 |
| cagr | -0.8419 |
| net_avg_win | 23.0873 |
| net_avg_loss | -39.5425 |
| avg_hold_time_bars | 15.2397 |
| exposure | 0.4884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
