# EMA Hourly Continuation — ONE/USDT P50_200

**Symbol:** ONE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7318 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0283 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.9084 |
| sortino_ratio | -0.5066 |
| max_drawdown | 0.4683 |
| cagr | -0.2111 |
| net_avg_win | 69.9547 |
| net_avg_loss | -95.5924 |
| avg_hold_time_bars | 25.1829 |
| exposure | 0.4006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
