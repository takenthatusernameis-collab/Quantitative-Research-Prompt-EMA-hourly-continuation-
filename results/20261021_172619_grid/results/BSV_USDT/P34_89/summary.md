# EMA Hourly Continuation — BSV/USDT P34_89

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6296 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.8800 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -3.0972 |
| sortino_ratio | -0.9676 |
| max_drawdown | 0.6802 |
| cagr | -0.3572 |
| net_avg_win | 50.4236 |
| net_avg_loss | -71.5414 |
| avg_hold_time_bars | 10.8727 |
| exposure | 0.2367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
