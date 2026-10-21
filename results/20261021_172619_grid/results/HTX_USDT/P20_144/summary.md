# EMA Hourly Continuation — HTX/USDT P20_144

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.5627 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8669 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -4.2932 |
| sortino_ratio | -1.2104 |
| max_drawdown | 0.7717 |
| cagr | -0.4363 |
| net_avg_win | 56.8665 |
| net_avg_loss | -80.1967 |
| avg_hold_time_bars | 31.8517 |
| exposure | 0.5636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
