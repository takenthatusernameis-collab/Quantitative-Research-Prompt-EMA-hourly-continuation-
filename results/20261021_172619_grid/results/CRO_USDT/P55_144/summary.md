# EMA Hourly Continuation — CRO/USDT P55_144

**Symbol:** CRO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7417 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0326 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -1.6669 |
| sortino_ratio | -0.4372 |
| max_drawdown | 0.4209 |
| cagr | -0.1812 |
| net_avg_win | 66.6932 |
| net_avg_loss | -93.7756 |
| avg_hold_time_bars | 16.7988 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
