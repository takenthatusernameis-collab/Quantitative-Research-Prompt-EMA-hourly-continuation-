# EMA Hourly Continuation — REZ/USDT P100_144

**Symbol:** REZ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.5389 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8347 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -4.3555 |
| sortino_ratio | -1.3890 |
| max_drawdown | 0.8051 |
| cagr | -0.4797 |
| net_avg_win | 42.0070 |
| net_avg_loss | -63.6708 |
| avg_hold_time_bars | 4.3589 |
| exposure | 0.0997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
