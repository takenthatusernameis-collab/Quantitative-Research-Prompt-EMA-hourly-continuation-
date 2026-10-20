# EMA Hourly Continuation — TFUEL/USDT P20_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 873 |
| net_profit_factor | 0.4946 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.8018 |
| gross_win_rate | 0.4296 |
| sharpe_ratio | -7.4220 |
| sortino_ratio | -3.0652 |
| max_drawdown | 0.9782 |
| cagr | -0.7768 |
| net_avg_win | 26.4193 |
| net_avg_loss | -37.8403 |
| avg_hold_time_bars | 9.3127 |
| exposure | 0.3679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
