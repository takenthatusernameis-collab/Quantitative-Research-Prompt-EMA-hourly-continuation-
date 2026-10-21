# EMA Hourly Continuation — TRX/USDT P12_200

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.6149 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9877 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.8445 |
| sortino_ratio | -0.7528 |
| max_drawdown | 0.5979 |
| cagr | -0.2968 |
| net_avg_win | 54.4816 |
| net_avg_loss | -88.6093 |
| avg_hold_time_bars | 40.8110 |
| exposure | 0.6381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
