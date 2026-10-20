# EMA Hourly Continuation — SNX/USDT P8_20

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1631 |
| net_profit_factor | 0.3986 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.8680 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -11.4274 |
| sortino_ratio | -6.5136 |
| max_drawdown | 0.9997 |
| cagr | -0.9609 |
| net_avg_win | 9.5466 |
| net_avg_loss | -17.7402 |
| avg_hold_time_bars | 3.0417 |
| exposure | 0.2245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
