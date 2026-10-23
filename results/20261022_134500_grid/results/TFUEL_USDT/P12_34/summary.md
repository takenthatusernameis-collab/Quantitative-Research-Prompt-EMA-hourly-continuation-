# EMA Hourly Continuation — TFUEL/USDT P12_34

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1423 |
| net_profit_factor | 0.4315 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.8272 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -11.9601 |
| sortino_ratio | -6.3680 |
| max_drawdown | 0.9997 |
| cagr | -0.9592 |
| net_avg_win | 13.5016 |
| net_avg_loss | -20.4236 |
| avg_hold_time_bars | 4.0253 |
| exposure | 0.2592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
