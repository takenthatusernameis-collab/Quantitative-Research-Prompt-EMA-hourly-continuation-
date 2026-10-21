# EMA Hourly Continuation — G/USDT P8_55

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.7189 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9447 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -2.6743 |
| sortino_ratio | -1.0047 |
| max_drawdown | 0.6720 |
| cagr | -0.3694 |
| net_avg_win | 55.5951 |
| net_avg_loss | -73.5385 |
| avg_hold_time_bars | 16.4288 |
| exposure | 0.5157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
