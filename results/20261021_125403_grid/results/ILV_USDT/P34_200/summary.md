# EMA Hourly Continuation — ILV/USDT P34_200

**Symbol:** ILV/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 1.0669 |
| net_win_rate | 0.5661 |
| gross_profit_factor | 1.2858 |
| gross_win_rate | 0.5661 |
| sharpe_ratio | 0.3986 |
| sortino_ratio | 0.0997 |
| max_drawdown | 0.1105 |
| cagr | 0.0379 |
| net_avg_win | 93.5284 |
| net_avg_loss | -114.3732 |
| avg_hold_time_bars | 39.9797 |
| exposure | 0.5361 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
