# EMA Hourly Continuation — SEI/USDT P12_34

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1287 |
| net_profit_factor | 0.5512 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8959 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -7.9335 |
| sortino_ratio | -4.0107 |
| max_drawdown | 0.9926 |
| cagr | -0.8580 |
| net_avg_win | 20.6279 |
| net_avg_loss | -31.7770 |
| avg_hold_time_bars | 3.9814 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
