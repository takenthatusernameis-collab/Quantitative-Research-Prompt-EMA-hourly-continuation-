# EMA Hourly Continuation — XLM/USDT P55_100

**Symbol:** XLM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.4001 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 1.0557 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -5.7836 |
| sortino_ratio | -2.0183 |
| max_drawdown | 0.9267 |
| cagr | -0.6415 |
| net_avg_win | 20.6779 |
| net_avg_loss | -47.9794 |
| avg_hold_time_bars | 5.4992 |
| exposure | 0.1547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
