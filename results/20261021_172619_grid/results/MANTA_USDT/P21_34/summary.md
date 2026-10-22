# EMA Hourly Continuation — MANTA/USDT P21_34

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6620 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -2.5964 |
| sortino_ratio | -0.6945 |
| max_drawdown | 0.5738 |
| cagr | -0.2725 |
| net_avg_win | 64.9149 |
| net_avg_loss | -88.4675 |
| avg_hold_time_bars | 5.2686 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
