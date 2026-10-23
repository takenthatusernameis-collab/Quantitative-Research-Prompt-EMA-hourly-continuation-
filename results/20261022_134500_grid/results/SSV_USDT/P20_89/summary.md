# EMA Hourly Continuation — SSV/USDT P20_89

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.5651 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8476 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -5.2978 |
| sortino_ratio | -2.0977 |
| max_drawdown | 0.9275 |
| cagr | -0.6315 |
| net_avg_win | 33.9325 |
| net_avg_loss | -47.8238 |
| avg_hold_time_bars | 10.6524 |
| exposure | 0.3827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
