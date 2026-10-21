# EMA Hourly Continuation — DBR/USDT P21_200

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.6114 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.7724 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -2.5014 |
| sortino_ratio | -0.6079 |
| max_drawdown | 0.4472 |
| cagr | -0.2451 |
| net_avg_win | 64.6210 |
| net_avg_loss | -84.7171 |
| avg_hold_time_bars | 45.2373 |
| exposure | 0.6071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
