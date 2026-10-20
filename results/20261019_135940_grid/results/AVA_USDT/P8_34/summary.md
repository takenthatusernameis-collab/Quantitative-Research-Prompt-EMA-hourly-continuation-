# EMA Hourly Continuation — AVA/USDT P8_34

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1335 |
| net_profit_factor | 0.4250 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.8210 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -8.6766 |
| sortino_ratio | -4.4462 |
| max_drawdown | 0.9961 |
| cagr | -0.8884 |
| net_avg_win | 12.2690 |
| net_avg_loss | -23.5657 |
| avg_hold_time_bars | 5.2172 |
| exposure | 0.3166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
