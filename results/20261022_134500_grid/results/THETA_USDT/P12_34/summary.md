# EMA Hourly Continuation — THETA/USDT P12_34

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1270 |
| net_profit_factor | 0.4756 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8556 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -8.7238 |
| sortino_ratio | -4.3902 |
| max_drawdown | 0.9955 |
| cagr | -0.8838 |
| net_avg_win | 16.0932 |
| net_avg_loss | -26.7748 |
| avg_hold_time_bars | 4.0181 |
| exposure | 0.2320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
