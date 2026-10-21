# EMA Hourly Continuation — ETHFI/USDT P20_34

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.7313 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9411 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -1.8171 |
| sortino_ratio | -0.4653 |
| max_drawdown | 0.4315 |
| cagr | -0.1926 |
| net_avg_win | 72.9801 |
| net_avg_loss | -93.1854 |
| avg_hold_time_bars | 6.4361 |
| exposure | 0.0939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
