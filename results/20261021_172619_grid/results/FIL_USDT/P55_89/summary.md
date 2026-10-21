# EMA Hourly Continuation — FIL/USDT P55_89

**Symbol:** FIL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.5521 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.7538 |
| gross_win_rate | 0.4358 |
| sharpe_ratio | -2.8250 |
| sortino_ratio | -0.6447 |
| max_drawdown | 0.5251 |
| cagr | -0.2566 |
| net_avg_win | 57.7977 |
| net_avg_loss | -80.8574 |
| avg_hold_time_bars | 6.6809 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
