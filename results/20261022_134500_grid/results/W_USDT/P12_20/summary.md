# EMA Hourly Continuation — W/USDT P12_20

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1475 |
| net_profit_factor | 0.4274 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.9020 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -11.3688 |
| sortino_ratio | -6.1792 |
| max_drawdown | 0.9996 |
| cagr | -0.9558 |
| net_avg_win | 11.7670 |
| net_avg_loss | -20.7566 |
| avg_hold_time_bars | 2.2034 |
| exposure | 0.1477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
