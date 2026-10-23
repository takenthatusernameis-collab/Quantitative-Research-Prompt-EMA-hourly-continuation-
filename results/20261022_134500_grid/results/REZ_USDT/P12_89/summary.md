# EMA Hourly Continuation — REZ/USDT P12_89

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.7421 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0082 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -2.5411 |
| sortino_ratio | -0.9370 |
| max_drawdown | 0.6812 |
| cagr | -0.3626 |
| net_avg_win | 57.1907 |
| net_avg_loss | -77.0689 |
| avg_hold_time_bars | 17.4482 |
| exposure | 0.5442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
