# EMA Hourly Continuation — XCH/USDT P12_144

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.9105 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.0813 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -0.5361 |
| sortino_ratio | -0.1587 |
| max_drawdown | 0.2181 |
| cagr | -0.0752 |
| net_avg_win | 82.0405 |
| net_avg_loss | -98.5794 |
| avg_hold_time_bars | 34.7447 |
| exposure | 0.6680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
