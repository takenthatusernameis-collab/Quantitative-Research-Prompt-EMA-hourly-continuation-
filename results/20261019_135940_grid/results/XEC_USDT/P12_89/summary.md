# EMA Hourly Continuation — XEC/USDT P12_89

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 785 |
| net_profit_factor | 0.5483 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8963 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -5.4230 |
| sortino_ratio | -2.1202 |
| max_drawdown | 0.9314 |
| cagr | -0.6462 |
| net_avg_win | 31.0942 |
| net_avg_loss | -48.5317 |
| avg_hold_time_bars | 15.2726 |
| exposure | 0.5425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
