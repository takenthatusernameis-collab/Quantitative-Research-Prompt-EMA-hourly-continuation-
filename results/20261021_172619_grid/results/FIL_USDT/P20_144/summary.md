# EMA Hourly Continuation — FIL/USDT P20_144

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7511 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -1.7001 |
| sortino_ratio | -0.4627 |
| max_drawdown | 0.4508 |
| cagr | -0.1921 |
| net_avg_win | 71.1146 |
| net_avg_loss | -88.1666 |
| avg_hold_time_bars | 30.5699 |
| exposure | 0.5072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
