# EMA Hourly Continuation — WIN/USDT P12_50

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6502 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9482 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -3.4691 |
| sortino_ratio | -1.2419 |
| max_drawdown | 0.7829 |
| cagr | -0.4341 |
| net_avg_win | 46.9716 |
| net_avg_loss | -67.3216 |
| avg_hold_time_bars | 10.6458 |
| exposure | 0.3020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
