# EMA Hourly Continuation — ETHFI/USDT P12_26

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1466 |
| net_profit_factor | 0.5135 |
| net_win_rate | 0.4284 |
| gross_profit_factor | 0.9497 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -10.1886 |
| sortino_ratio | -5.5028 |
| max_drawdown | 0.9990 |
| cagr | -0.9342 |
| net_avg_win | 16.7867 |
| net_avg_loss | -24.5004 |
| avg_hold_time_bars | 2.8909 |
| exposure | 0.1926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
