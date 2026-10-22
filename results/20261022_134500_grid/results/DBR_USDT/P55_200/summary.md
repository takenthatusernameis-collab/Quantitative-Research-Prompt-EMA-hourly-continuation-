# EMA Hourly Continuation — DBR/USDT P55_200

**Symbol:** DBR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.4876 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.7914 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -4.3332 |
| sortino_ratio | -1.1621 |
| max_drawdown | 0.6918 |
| cagr | -0.4363 |
| net_avg_win | 50.4306 |
| net_avg_loss | -79.8905 |
| avg_hold_time_bars | 20.8818 |
| exposure | 0.3515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
