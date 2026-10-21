# EMA Hourly Continuation — ICP/USDT P8_100

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.8343 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0179 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.2225 |
| sortino_ratio | -0.3803 |
| max_drawdown | 0.3988 |
| cagr | -0.1627 |
| net_avg_win | 76.1035 |
| net_avg_loss | -93.1753 |
| avg_hold_time_bars | 31.5732 |
| exposure | 0.6760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
