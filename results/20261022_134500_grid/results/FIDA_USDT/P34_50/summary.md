# EMA Hourly Continuation — FIDA/USDT P34_50

**Symbol:** FIDA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 890 |
| net_profit_factor | 0.3289 |
| net_win_rate | 0.4067 |
| gross_profit_factor | 0.7657 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -9.1202 |
| sortino_ratio | -3.8661 |
| max_drawdown | 0.9925 |
| cagr | -0.8548 |
| net_avg_win | 13.4350 |
| net_avg_loss | -28.0049 |
| avg_hold_time_bars | 3.5416 |
| exposure | 0.1426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
