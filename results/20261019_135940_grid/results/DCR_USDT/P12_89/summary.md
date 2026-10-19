# EMA Hourly Continuation — DCR/USDT P12_89

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 873 |
| net_profit_factor | 0.5149 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.7938 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -5.9916 |
| sortino_ratio | -2.4669 |
| max_drawdown | 0.9556 |
| cagr | -0.7018 |
| net_avg_win | 26.1966 |
| net_avg_loss | -40.3271 |
| avg_hold_time_bars | 12.4971 |
| exposure | 0.4937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
