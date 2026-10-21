# EMA Hourly Continuation — BTT/USDT P12_26

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -5.5138 |
| sortino_ratio | -1.6943 |
| max_drawdown | 0.8648 |
| cagr | -0.5464 |
| net_avg_win | 41.4120 |
| net_avg_loss | -69.2404 |
| avg_hold_time_bars | 6.4298 |
| exposure | 0.1312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
