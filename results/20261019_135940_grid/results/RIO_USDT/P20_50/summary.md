# EMA Hourly Continuation — RIO/USDT P20_50

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1130 |
| net_profit_factor | 0.5188 |
| net_win_rate | 0.4115 |
| gross_profit_factor | 0.7709 |
| gross_win_rate | 0.4159 |
| sharpe_ratio | -7.9817 |
| sortino_ratio | -3.7836 |
| max_drawdown | 0.9898 |
| cagr | -0.8412 |
| net_avg_win | 22.9448 |
| net_avg_loss | -30.9269 |
| avg_hold_time_bars | 4.4168 |
| exposure | 0.2291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
