# EMA Hourly Continuation — VR/USDT P12_20

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.5143 |
| net_win_rate | 0.3941 |
| gross_profit_factor | 0.7517 |
| gross_win_rate | 0.4068 |
| sharpe_ratio | -3.6528 |
| sortino_ratio | -0.7927 |
| max_drawdown | 0.6118 |
| cagr | -0.3139 |
| net_avg_win | 69.6598 |
| net_avg_loss | -88.0845 |
| avg_hold_time_bars | 7.8517 |
| exposure | 0.0842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
