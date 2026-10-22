# EMA Hourly Continuation — UMA/USDT P12_200

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8244 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.1310 |
| sortino_ratio | -0.3209 |
| max_drawdown | 0.3313 |
| cagr | -0.1388 |
| net_avg_win | 73.8154 |
| net_avg_loss | -91.8445 |
| avg_hold_time_bars | 36.9771 |
| exposure | 0.6605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
