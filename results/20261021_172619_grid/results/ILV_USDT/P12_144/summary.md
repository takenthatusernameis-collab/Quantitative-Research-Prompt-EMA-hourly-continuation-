# EMA Hourly Continuation — ILV/USDT P12_144

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.9000 |
| net_win_rate | 0.5217 |
| gross_profit_factor | 1.0898 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -0.6288 |
| sortino_ratio | -0.1734 |
| max_drawdown | 0.2691 |
| cagr | -0.0803 |
| net_avg_win | 88.9334 |
| net_avg_loss | -107.7957 |
| avg_hold_time_bars | 40.7147 |
| exposure | 0.6810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
