# EMA Hourly Continuation — NEO/USDT P12_55

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.4403 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.8255 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -7.5217 |
| sortino_ratio | -3.3537 |
| max_drawdown | 0.9834 |
| cagr | -0.8043 |
| net_avg_win | 17.4599 |
| net_avg_loss | -31.4844 |
| avg_hold_time_bars | 8.5704 |
| exposure | 0.3900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
