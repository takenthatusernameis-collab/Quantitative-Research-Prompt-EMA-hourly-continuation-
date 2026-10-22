# EMA Hourly Continuation — HBAR/USDT P12_89

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.6082 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9512 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -4.4486 |
| sortino_ratio | -1.7453 |
| max_drawdown | 0.8982 |
| cagr | -0.5679 |
| net_avg_win | 36.3648 |
| net_avg_loss | -55.6362 |
| avg_hold_time_bars | 14.2506 |
| exposure | 0.5040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
