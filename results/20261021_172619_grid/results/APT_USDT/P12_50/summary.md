# EMA Hourly Continuation — APT/USDT P12_50

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9589 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -2.0077 |
| sortino_ratio | -0.6918 |
| max_drawdown | 0.5841 |
| cagr | -0.2726 |
| net_avg_win | 58.4409 |
| net_avg_loss | -76.0285 |
| avg_hold_time_bars | 11.9207 |
| exposure | 0.3143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
