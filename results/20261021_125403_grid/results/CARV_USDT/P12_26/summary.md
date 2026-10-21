# EMA Hourly Continuation — CARV/USDT P12_26

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6738 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9870 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -3.0077 |
| sortino_ratio | -1.0600 |
| max_drawdown | 0.6307 |
| cagr | -0.3843 |
| net_avg_win | 53.2278 |
| net_avg_loss | -78.6703 |
| avg_hold_time_bars | 6.3984 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
