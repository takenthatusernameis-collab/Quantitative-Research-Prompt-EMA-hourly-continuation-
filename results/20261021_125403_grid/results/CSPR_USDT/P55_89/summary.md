# EMA Hourly Continuation — CSPR/USDT P55_89

**Symbol:** CSPR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7213 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9534 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.7078 |
| sortino_ratio | -0.4069 |
| max_drawdown | 0.3831 |
| cagr | -0.1702 |
| net_avg_win | 71.7158 |
| net_avg_loss | -94.5192 |
| avg_hold_time_bars | 6.8014 |
| exposure | 0.0856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
