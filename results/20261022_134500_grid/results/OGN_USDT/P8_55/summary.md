# EMA Hourly Continuation — OGN/USDT P8_55

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 1.0203 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -5.5157 |
| sortino_ratio | -2.4223 |
| max_drawdown | 0.9484 |
| cagr | -0.6893 |
| net_avg_win | 34.6738 |
| net_avg_loss | -48.9470 |
| avg_hold_time_bars | 11.2500 |
| exposure | 0.5030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
