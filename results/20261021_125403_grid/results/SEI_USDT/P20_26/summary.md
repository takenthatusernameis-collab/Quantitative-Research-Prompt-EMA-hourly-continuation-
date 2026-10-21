# EMA Hourly Continuation — SEI/USDT P20_26

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 0.7048 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9762 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -1.5013 |
| sortino_ratio | -0.2846 |
| max_drawdown | 0.2979 |
| cagr | -0.1226 |
| net_avg_win | 77.7321 |
| net_avg_loss | -106.5669 |
| avg_hold_time_bars | 4.7086 |
| exposure | 0.0375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
